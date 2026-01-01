import hashlib
from pathlib import Path

import json
import os
from typing import Dict, List

from openai import OpenAI

from analyzer.base import Analyzer
from utils import load_environment_variables

class LLMAnalyzer(Analyzer):
    """
    Analyzer implementation that uses OpenAI LLMs.
    """
    CACHE_PATH = Path("cache/llm_cache.json")
    
    def _get_cache_key(self, description: str) -> str:
        """
        Generate a deterministic cache key from job description.
        """
        return hashlib.sha256(description.encode("utf-8")).hexdigest()


    def analyze(self, description: str) -> Dict[str, List[str] | str]:
        """
        Analyze a job description using an LLM and return structured JSON output.

        Expected output format:
        {
            "skills": ["python", "apis"],
            "seniority": "junior | mid | senior | unknown" 
        }
        """
        cache_key = self._get_cache_key(description)

        # Load cache
        if self.CACHE_PATH.exists():
            with open(self.CACHE_PATH, "r", encoding="utf-8") as f:
                cache = json.load(f)
        else:
            cache = {}

        # Return cached result if present
        if cache_key in cache:
            return cache[cache_key]

        
        #Load environment variables (.env)
        load_environment_variables()

        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise RuntimeError("OPENAI_API_KEY is not set")
        
        client = OpenAI(api_key=api_key)

        #System message enforces behavior
        system_prompt = (
            "You are an information extraction system."
            "Return ONLY valid JSON."
            "Do not include explanations or extra text."
        )

        user_prompt = (
            "Extract the following fields from the job description:\n"
            "- skills (as a list of lowercase strings)\n"
            "- seniority (one of: junior, mid senior, unknown)\n\n"
            f"Job description:\n{description}"
        )

        response = client.chat.completions.create(
            model = "gpt-4o-mini",
            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0,
        )

        raw_output = response.choices[0].message.content
        raw_output = raw_output.strip()

        # Handle common case where JSON is wrapped in Markdown code fences
        if raw_output.startswith("```"):
            raw_output = raw_output.strip("`")
            # Remove optional 'json' label
            if raw_output.lower().startswith("json"):
                raw_output = raw_output[4:].strip()

        try:
            parsed = json.loads(raw_output)

            # Persist to cache
            cache[cache_key] = parsed
            with open(self.CACHE_PATH, "w", encoding="utf-8") as f:
                json.dump(cache, f, indent=2)

            return parsed

        except json.JSONDecodeError as e:
            raise ValueError(f"LLM returned invalid JSON: {raw_output}") from e
        