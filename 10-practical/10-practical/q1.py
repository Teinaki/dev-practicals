

class PostComment:
    """PostComment can be used to represent a comment or a tag added to a blog post."""
    def __init__(self, blogpost, message):
        if message[0] == '#':
            # it's a tag
            blogpost.add_tag(message)
        else:
            blogpost.add_comment(message)
"""open closed is violated so I split into subclasses for a tag or comment"""

class Tag(PostComment):
    def __init__(self, blogpost, message):
        blogpost.add_tag(message)

class Comment(PostComment):
    def __init__(self, blogpost, message):
        blogpost.add_comment(message)

class PostComment:
    """PostComment can be used to represent a comment or a tag added to a blog post."""
    def __init__(self, blogpost, message):
        if message[0] == '#':
            # it's a tag
            blogpost.add_tag(message)
        else:
            blogpost.add_comment(message)
# The idea here is that we hava BlogPost class that represents, well, blog
# posts. Somebody might read the post and want to add either a comment or
# a tag. This violates the open/closed principle. The giveaway is the if/else
# bit. Suppose we want to add a new kind of BlogPost attachment, like a link
# or a social media share? Then we're going to have to modify that if/else
# block. You get into this mess by starting with just a basic comment class,
# and then adding special cases over time
# You could also argue that this violates single responsibility, but I think the
# open/closed principle is a better fit.
# We fix this by breaking this up into distinct classes
class PostFollowUp(ABC):
    pass
class PostComment(PostFollowUp):
    pass
class PostTag(PostFollowUp):
    pass
class SocialMediaShare(PostFollowUp):
    pass

# Soon we'll see that this could be a good place to use the Factory or AbstractFactory pattern.