import re
def text_redactor(text,sensitive_terms):
    try:
        for term in sensitive_terms:
            #escape special characters like @,. and etc
            pattern=re.escape(term)
            text=re.sub(pattern,"[REDACTED]",text,flags=re.IGNORECASE)
        return text
    except Exception as e:
        return f"error during redaction : {e}"
text="Contact Alex at alex@corp.com" 
sensitive_terms=["Alex", "alex@corp.com"]
print(text_redactor(text,sensitive_terms))