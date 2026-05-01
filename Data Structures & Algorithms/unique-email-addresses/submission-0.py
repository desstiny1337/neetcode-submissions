class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniqueEmails = set()
        for email in emails:
            name, domain = email.split("@")

            name = name.split("+")[0]
            name = name.replace(".", "")
            finalMail = name+"@"+domain
            uniqueEmails.add(finalMail)

        return len(uniqueEmails)

        