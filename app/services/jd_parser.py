import subprocess
import json 

def parse_jd(jd_texts: str) -> dict:
    prompt = f"""
      Extract the following fields from this job description and return as JSON
        only, no extra text:
      - company
      - role
      - location
      - salary
      - notes (a brief summary)

      Job description:
      {jd_text}
      """
    result = subprocess.run(
        ['claude', '-p', prompt],
        capture_output=True,
        text=True 
    )

    raw = result.stdout.strip() 
    return json.load(raw) 
