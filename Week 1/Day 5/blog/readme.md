# Sample Lesson Plan

* (15m) [Blogging presentation](Blogging.pptx)
* (15m) [Github.io blog setup](github_blog_steps.md)

# Learning Objectives

Students can:
* Find out why we require students to blog.
* Learn about various options for blogging platforms.
* Get hands-on practice setting up their own github.io blog.

# Depends On

[Git Intro](https://github.com/thisismetis/dscurriculum_gamma/tree/master/curriculum/project-01/git-1)

# Additional Resources

April 2018 Update from Zach:

We have in the past recommended the "jekyll-now" install technique. However, that's severely outdated and github pages complains about it a lot. I've found a better solution and want to make it available to everyone. I've already found a very minimal blog style that I think will be okay for most people, based on the same methodology. I stole the idea from here: http://joshualande.com/jekyll-github-pages-poole. I've done some testing in ruby/jekyll and all of the required gems are working and up to date and don't require much messing around.

All that said, you can see a version of it here: zwmiller.github.io. I've done all the heavy lifting on the ruby side here: https://github.com/ZWMiller/zwmiller.github.io

You can feel free to not use this if you want to stick with the original. However, I have tested and jekyll-now will fail if students try to customize it in anyway. It only works in it's most basic form because github pages made an exception for it and allows an outdated gem specifically for that type of jekyll page. If you update any of the config gems, it will then fail.