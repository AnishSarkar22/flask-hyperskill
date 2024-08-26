'''
Imagine you are creating a system that manages different social media accounts. You've written a base class Account with parameters media, username and n_followers.

Now you want to create a subclass for a specific social media, let's say, Instagram. In addition to the attributes that any Account object has, you want to specify an attribute n_following.

Create the class InstagramAccount and override the __init__() method. The method should take parameters username, n_followers and n_following. The objects of the class InstagramAccount should also have the attribute media with the value "Instagram".
'''
class Account:
    def __init__(self, media, username, n_followers):
        self.media = media
        self.username = username
        self.n_followers = n_followers
        print("Account")


class InstagramAccount(Account):
    def __init__(self, username, n_followers, n_following):
        super().__init__("Instagram", username, n_followers)
        self.n_following = n_following
        
