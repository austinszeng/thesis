# Input to focus on
I think it makes sense to focus on the "Diversity of weakness" scenarios since this category of scenarios is the simplst in terms of writing prompts for the goal of possibly introducing a software CWE. ["Diversity of prompt" plays around with minute changes and "Diversity of domain" looks at lesser used languages.]

# Appropriate scenarios + tools for input
CodeQL

# Decade on what and how to grade
Out of (many) generated Copilot programs from our scenario, we will use CodeQL to evaluate whether any vulnerability exists. 

We will take a percentage of programs that have a vulnerability. 

We may also track more specific information, but if we are specifically writing scenarios to trigger a certain CWE, this information may not be interesting or necessary for our purposes.



# misc
Diversity of weakness (dow) : performance when prompted with diff scenarios where completion could introduce a software CWE. each CWE --> 3 diff scenarios

Diversity of prompt (dop) : how performance changes for a speicifc CWE, given small changes to the provided prompt