# EZ-AI-Scripting
Lets anyone train a language model using Tensor Flow.
You'll need to install python3, and any dependencies that the scripts may use. Those modules are listed at the top of the scripts, and python3 interpreter will yell at you if you don't have them installed. Recommended to use ubuntu/linux instead of windows.

1) What you'll want to do first: run the training script. Select a document that you'd like to train the transformer on.
2) It will save to a wordembeddings.txt file in the parent directory. Take a look. Now just run the beam_search script.

There are a few numbers you can alter in the scripts, as well. dim_embedding in 'training' is set to 1 dimension but can go up to ridiculous numbers. Epochs may go up or down depending on what kind of resolution you really want. Window size, learning rate can be adjusted as well. In the beam_search script, you can change the number of beams, the length of the beams, and there are some other interesting things you can do but I didn't include them in the script. 
