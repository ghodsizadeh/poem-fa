from poem_fa import Hafez


def test_hafez_fal():
    res = Hafez().fal()
    for i, verse in enumerate(res):
        assert i+1 == verse[0]
        assert verse[1] == i % 2
