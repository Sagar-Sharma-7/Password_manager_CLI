from passlib.hash import sha256_crypt
with open("m_pwd.key", "rb") as f:
    m_pwd = f.read()
    password = m_pwd
    print(sha256_crypt.verify("pythonisbest", password))



