from Naked.toolshed.shell import execute_js, muterun_js


def RunNodeScript():
    from Naked.toolshed.shell import execute_js, muterun_js
    result = execute_js('CCW/static/JS/getTweetLocations.js')

    if result:
        print('Succesfull')
    else:
        print('Unsuccesfull')
    