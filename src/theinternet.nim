import asyncdispatch, asyncnet, strutils
import jester, htmlgen, cgi, logging
import osproc, terminal

import jester, json
import strmisc, strutils
import unicode

settings:
  port = Port(8080)
  bindAddr = "127.0.0.1"

proc layout(content: string): string = htmlgen.html(htmlgen.body(
    script(src="/nim.js", `type`="text/javascript"),
    script(src="/client.js", `type`="text/javascript"),
    link(href="/app.css", rel="stylesheet"),
    content
))

routes:
  get "/":
    var name = "" & request.host.partition(".")[0]
    name = name.replace('_', ' ')

    var content = `div`(
        `div`(
          h2("Hello, I am " & name.title() & "."),
          h1("I am from The Internet."),
        ))
    
    resp layout(content)

  get "/app.css":
    const appCSS = staticRead "static/app.css"
    resp appCSS