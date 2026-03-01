from pyscript import display, document


def click(e):
    document.getElementById('output').innerHTML = ' '
    players = ['Villanueva', 'Quinn', 'Legarda', 'Arthurs', 'Tolentino', 'Fuentes', 'Santos', 'Flores', 'Martin', 'Lewis', 'Raymonds', 'Way']
    
    for player in players:
        display(player, target='output')



   