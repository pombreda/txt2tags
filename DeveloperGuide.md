If you have any doubt, please contact Aurelio: [mailto:verde@aurelio.net](mailto:verde@aurelio.net), [@aureliojargas](http://twitter.com/aureliojargas), or aureliojargas (Google Talk).

# Before you start #

Make sure you have the newest code:

```
svn update
```

# Good Practices #

  * Feel free to add a new target.
  * Feel free to add a new rule.
  * Do not submit two or more different issues in a single commit. If you want to fix two bugs, make two separated commits.
  * Do not use short options (like -s, -c) for new features. Talk to Aurelio if you think the feature is important enough to deserve a short option.
  * Talk to Aurelio before adding a new mark, %%macro or %!command, they may violate the KISS principle.
  * If your patch is complex or may alter txt2tags in a substancial way, talk to Aurelio first -- KISS principle under attack! :)
  * If you have an incomplete or unstable work to commit, create a new branch. See instructions at this page.

# Coding style #

The current code is PEP-8 compatible, with a few exceptions for visual alignment of dictionary keys and variable setting. Long lines (>80) are also allowed.

Use the `dist/check-code.sh` script to check if the code is following the rules.

Please read [PEP-8](http://www.python.org/dev/peps/pep-0008/) for details about the code syntax.

A quick summary:

  * Use 4 spaces for indentation, not TABs.
  * Use just one command per line.
  * Use spaces around operators: `a = 1 + 2` not `a=1+2`
  * Prefer descriptive names for variables and functions: `table_row` not `tr`
  * Avoid global variables.
  * Use Unix line breaks (LF), not Windows (CR+LF).

Other:

  * Comment your code.
  * Avoid Python's new commands and features, to make txt2tags compatible with old Python versions. Stick with Python 2.3 features.

Useful reading:

  * For a quick reference, the [Google Python Style Guide](http://google-styleguide.googlecode.com/svn/trunk/pyguide.html) is a good read.

# Debug #

You can use the `--debug` option to see what's going on behind the curtain when converting a file.

# Commits #

## 1. TEST your code ##

  * You really fixed that bug?
  * Your new target is really working?
  * Your new feature is working for all targets?

Make extensive tests to make sure your code really do want you want it to do.

## 2. ALWAYS run the test suite and check-code.sh ##

The test suite must be 100% for you to commit. If you find any error, fix it before the commit.

```
cd test
python run.py
```

Also, check if your code is ok:

```
./dist/check-code.sh
```

## 3. Make a diff to review your changes ##

Make sure you're changing just what you meant to.

```
svn diff
```

Tip: Use your text editor to review the changes with nice colors:

```
svn diff | vim -     # Vim

svn diff | mate      # TextMate
```

## 4. Compose the log message ##

It's very important that you write an **informative** message that describes what changes you are committing.

  * Explain what your commit does.
  * Write long messages if necessary.
  * It's best to write more than less.

If you're changing a specific target, prefix the message with it. Example:

  * **DocBook:** Now special chars are escaped: &, <, >

If you're closing an issue, append this to the end of your message: (closes issue N), where N is the issue number. Example:

  * DocBook: Now special chars are escaped: &, <, > **(closes [issue 86](https://code.google.com/p/txt2tags/issues/detail?id=86))**

If you're referring to changes made in another commit, use rNN where NN is the revision number. Example:

  * HTML: Fixing bold tag to respect changes made in **[r78](https://code.google.com/p/txt2tags/source/detail?r=78)**.

If you're adding a new target, follow this format:

  * New target AsciiDoc (-t adoc). See http://www.methods.co.nz/asciidoc/

If you're adding a new translation, follow this format:

  * New translation: Markup Demo in French
  * New translation: Sample File in French
  * New translation: Manual Page in French
  * New translation: program messages in French

If you're adding an extra, like text editor syntax files, add the prefix extra:

  * **extra:** Added syntax file for "le" text editor

## 5. Everything is ok? Make the commit ##

```
svn commit -m "Your nice detailed log message"
```

# Branches #

Branches are used as a separate area where you can refine your work until it's stable and ready for production (trunk).

When you have a new idea or feature to experiment, first create a new branch then add your code to it. When you think it's ready, merge the branch changes into trunk.

## Create a branch ##

To create a branch it's just a single command line, you don't even need to have a local copy of trunk. This was the command I used to create the python3 branch:

```
svn copy https://txt2tags.googlecode.com/svn/trunk/ \
        https://txt2tags.googlecode.com/svn/branches/python3 \
        -m "Creating a branch of trunk for code compatible with Python 3."
```

Just change "python3" and the log message and the new branch is done.

## Checkout your new branch ##

Checkout the new branch you just created so you can work on it:

```
svn checkout https://txt2tags.googlecode.com/svn/branches/python3/ python3 --username aureliojargas
```

Of course, change "python3" and "aureliojargas" by your own data.

Happy coding! :)