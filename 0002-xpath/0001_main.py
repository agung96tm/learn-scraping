from lxml import html

# Sample HTML
html_content = """
<html>
    <body>
        <div id="main">
            <article class="main-article" style="height: auto !important;">
                <h1>Anaconda (1997) - full transcript</h1>
                <p class="plot-1">
                    When a documentary crew traveling through the Amazon jungle, picks up a stranded man, 
                    they are unaware of the trouble that will occur. This stranger's hobby is to capture 
                    the giant Anaconda snake, and plans to continue targeting it on their boat, 
                    by any means necessary.
                </p>
                
                <p class="plot-2">
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut 
                    labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco 
                    laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in 
                    voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat 
                    cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.   
                </p>

                <div class="full-script">
                    foodval.com - stop by if you're interested in the nutritional composition of food <br> --- <br>
                    Please, help. Somebody, help.<br><br>- Miss Flores.<br>- Professor Cale.<br><br>Come on in. When did you get in?
                    <br><br>A couple of days ago.<br>I've been talking to some guides...<br><br>...
                    hoping they might know the whereabouts our tribe.<br><br>Any luck?<br><br>
                    Well, Looks like there's sufficient evidence to suspect<br>these people are out there...<br><br>...
                    can be found and studied.<br><br>At least, that's what I told the grant people.
                    <br><br>My man seems to think that the tribe was somewhere around here...
                    <br><br>...between these two tributaries.<br>He'd found one of their markers.
                </div>
            </article>
        </div>
    </body>
</html>
"""

tree = html.fromstring(html_content)

"""
===========================================
XPath Syntax
===========================================

tagName[@AttributeName="Value"]

"""

titles1 = tree.xpath('//h1')
print(titles1[0].text_content())

pages = tree.xpath('//p[1]')
print(pages[0].text_content())

full_script = tree.xpath('//div[@class="full-script"]')
print(full_script[0].text_content())

print("-------")


"""
===========================================
XPath Functions
https://developer.mozilla.org/en-US/docs/Web/XPath/Functions
===========================================

contains()
starts-with()

[Example]
tagName[contains(@AttributeName, "Value")]
tagName[(expression1) and (expression2)]

"""
plots_2 = tree.xpath('//p[contains(@class, "plot")]')
for plot in plots_2:
    print(plot.text_content())
