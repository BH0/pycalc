req := ComObjCreate("Msxml2.XMLHTTP")
; Open a request with async enabled.

route = http://whitesmokeremorsefuldeal--five-nine.repl.co/
InputBox, input, Calc, What is your calculation (methods dissallowed)?
url := StrReplace(input, "/", "div")
url := StrReplace(url, ".", "dot")
MsgBox, %url%
req.open("GET", "http://whitesmokeremorsefuldeal--five-nine.repl.co/calc/"url, true)
req.onreadystatechange := Func("Ready")
req.send()

/*
; If you're going to wait, there's no need for onreadystatechange.
; Setting async=true and waiting like this allows the script to remain
; responsive while the download is taking place, whereas async=false
; will make the script unresponsive.
while req.readyState != 4
    sleep 100
*/

#Persistent

Ready() {
    global req
    if (req.readyState != 4)  ; Not done yet.
        return
    if (req.status == 200) ; OK.
        MsgBox % "Latest AutoHotkey version: " req.responseText
    else
        MsgBox 16,, % "Status " req.status
    ExitApp
}