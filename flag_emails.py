# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 23:24:07 2021

@author: Arjun Krishnan





"""


import os

from email.parser import Parser


# Function expecting the emails to be in "enron_email_corpus/maildir" folder and this
# folder structure is expected to be in the source directory

def emails_between(suspects):
    """
    

    Parameters
    ----------
    suspects : dictionary
        contains the names of flagged inidviduals as key and there list of the suspects emails
        as the values.

    Returns
    -------
    flagged_emails : list
        a list containing selected email.message.Message object.

    """
    folder_root = "enron_email_corpus/maildir"
    flagged_emails = []
    suspect_emails = [v for k, v in suspects.items()]
    print("Suspect Emails ", suspect_emails)
    email_contents_dir = os.path.join(os.getcwd(), folder_root)
    print(os.path.join(os.getcwd(), folder_root))
    if os.path.exists(email_contents_dir):
        account_names = os.listdir(email_contents_dir)
        for account_name in account_names:
            rootdir = os.path.join(email_contents_dir, account_name)
            for dirName, subDirList, fileList in os.walk(rootdir):
                for file in fileList:
                    email_path = os.path.join(dirName, file)
                    from_flag = False
                    to_flag = False
                    with open(email_path, 'r') as fp:
                        try:
                            headers = Parser().parse(fp)
                            if len(headers['To'].split()) <= 20:
                                for k, v in suspects.items():
                                    if headers['From'] in v:
                                        from_flag = True
                                    if headers['To'] in v:
                                        to_flag = True
                            if from_flag and to_flag:
                                flagged_emails.append(headers)
                        except:
                            print("Oops!!! Something is wrong with the email")
    return flagged_emails


if __name__ == "__main__":
    red_flags = {"lay-k": ["kenneth.lay@enron.com", "klay@enron.com"],
                 "skilling-j": ["skilling@enron.com", "jeff.skilling@enron.com"]}
    emails = emails_between(red_flags)
    print(emails)
