class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        seen = set()
        final_email = ""
        final_local = ""
        for email in emails:
            for i in range(0,len(email)):
                if email[i] == '@':
                    local_name = email[0:i]
                    domain_name = email[i+1:]
                    break
        
            final_local = local_name.split('+')[0].replace('.', '')
        
            final_email = final_local + '@' + domain_name
            seen.add(final_email)
        
        return len(seen)
