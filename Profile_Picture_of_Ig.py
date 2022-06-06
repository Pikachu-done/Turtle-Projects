# import instaloader
# print("\n---- | Download Instagram profile picture | ----\n")

# class Downloader:
#     def __init__(self, username):
#         self.username = username
#     def __repr__(self):
#         try:
#             self.get_profile_picture(self.username)
#             return (f"\nProfile picture of \"{self.username}\" downloaded successfully.\n")
#         except:
#             return (f"\nUser \"{self.username}\" does not exist.\n")

#     # methods
#     def get_profile_picture(self, user):
#         session = instaloader.Instaloader()
#         session.download_profile(user, profile_pic_only=True)
#         return 0

# # main execution
# if __name__ == "__main__":
#     # user interaction
#     username = input("Enter username: ")
#     print(Downloader(username))


import instaloader
print("\n---- | Download Instagram profile picture | ----\n")

root=instaloader.Instaloader()
usr_name=input("Enter User Name :")
print(root.download_profile(usr_name,profile_pic_only=True))