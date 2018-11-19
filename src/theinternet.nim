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
    # link(href="/app.css", rel="stylesheet"),
    content
))

routes:
  get "/":
    echo request.headers
    var name = request.headers["X-Forwarded-Host"].partition(".")[0]
    name = name.replace('_', ' ')

    var content = `div`(
        `div`(
          h2("Hello, I'm " & name.title() & ".", style="text-align: center;"),
          h1("I am from The Internet.", style="text-align: center;"),
        ))
    
    resp layout(content)
