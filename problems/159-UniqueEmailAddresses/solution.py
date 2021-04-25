class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        mails = set()
        for item in emails:
            l_name, domain = item.split("@", 1)
            l_name = l_name.split('+')[0].replace('.', '')
            mail = f"{l_name}@{domain}"
            mails.add(mail)
        return len(mails)