so i think most of my code is parallelized, since opencv does that by itself. 
however to test it, i toyed around with cv2.setUseOptimized(False) and cv2.setNumThreads(1)
and did not notice anything slowing down...
not sure what that means exactly

maybe the operations i use are not parallelized by opencv or intensive enough, since the testscript shows it does actually work. 
i could invest more time and try to get to the bottom of this and optimize my script, but I don't really feel like it...
