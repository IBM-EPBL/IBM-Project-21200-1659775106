import pickle
from pathlib import Path
import streamlit_authenticator as stauth

names = ["Ahamed Basheer M","Aishwarya DP","Amreen Taj MA","Lokesh M"]
usernames = ["Ahamed-1","DP-Ash","Amreen-Taj","Loki-1"]
passwords = ["Ahamed@123","Aishwarya@123","Amreen@123","Lokesh@123"]

hashed_passwords=stauth.Hasher(passwords).generate()
file_path=Path(__file__).parent/ "pwd.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords,file)