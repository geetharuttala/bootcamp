from models.paper import Paper, Figure, Entity

def test_entity_model():
    e = Entity(text="BRCA1", type="Gene", start=10, end=15)
    assert e.text == "BRCA1"
    assert e.type == "Gene"
    assert e.start == 10
    assert e.end == 15

def test_figure_model():
    f = Figure(
        caption="Some caption",
        label="Figure 1",   # 🔧 Add this line
        url="http://example.com",
        entities=[Entity(text="TP53", type="Gene", start=5, end=9)]
    )
    assert f.caption == "Some caption"
    assert f.label == "Figure 1"
    assert f.url == "http://example.com"
    assert len(f.entities) == 1
    assert f.entities[0].text == "TP53"

def test_paper_model():
    paper = Paper(
        paper_id="PMC123456",
        title="Some Title",
        abstract="Some abstract text",
        figures=[]
    )
    assert paper.paper_id == "PMC123456"
    assert paper.title == "Some Title"
