def sudy_nebo_lichy(cislo):
    if cislo % 2 == 0:
        return "sudy"
    else:
        return "lichy"
    
def test_sudy_nebo_lichy():
    assert sudy_nebo_lichy(1) == "lichy"
    assert sudy_nebo_lichy(2) == "sudy"

