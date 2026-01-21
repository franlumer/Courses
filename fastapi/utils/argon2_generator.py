from passlib.context import CryptContext

crypt = CryptContext(schemes=["argon2"])
print(crypt.hash("123456")) # $argon2id$v=19$m=65536,t=3,p=4$KMW4d661dg7h/P9fa21N6Q$xXzHvesRRMBN5gbGlElJu93if4jx+YmBrPndLyU1W/c
print(crypt.hash("654321")) # $argon2id$v=19$m=65536,t=3,p=4$8773nlPqvbeWcs6ZU8r5fw$5X0wTR+ELmdB/7/IxLOfO9w8L/BQy0CC1eeg5Pk9PMk