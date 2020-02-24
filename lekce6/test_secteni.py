from secteni import secti

def test_secti():
    assert secti(1, 2) == 3

## Příkaz assert vyhodnotí výraz za ním a pokud výsledek není pravdivý, vyvolá výjimku, která způsobí, že test selže. Můžeš si představit, že assert a == b dělá následující:

#if not (a == b):
#    raise AssertionError('Test selhal!')