from LMS.lms import LMS

# navigates to login page, logs in,
# & downloads each subject's syllabus
# to change subject ids, read README.md
with LMS() as lms:
    lms.login_page()
    lms.login()
    lms.download_subject('40777')
    lms.download_subject('40775')
    lms.download_subject('40776')
    lms.download_subject('40778')
    lms.download_subject('40779')