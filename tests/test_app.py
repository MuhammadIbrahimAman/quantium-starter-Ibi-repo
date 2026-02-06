# Importing our app.py from main application
from app import app

# Test 1: Verifies that header in the app is present
def test_header_present(dash_duo):
    # Start the Dash app
    dash_duo.start_server(app)

    # Find the header element
    header = dash_duo.find_element("h1")

    # Check that if it exists
    assert header is not None

    # Check that it contains the title when dash app is loaded
    assert "Pink" in header.text or "Morsel" in header.text

# Test 2: Verifies that graph is displayed in the app
def test_graph_present(dash_duo):
    dash_duo.start_server(app)

    # Find the graph by ID
    graph = dash_duo.find_element("#sales-line-chart")
    
    # Check if the graph is present
    assert graph is not None


# Test 3: Verifies that radio buttons for region filtering is present in the app
def test_region_picker_present(dash_duo):
    dash_duo.start_server(app)

    # Find the radio items by ID
    radio = dash_duo.find_element("#region-filter")
    
    # Checks that radio buttons are present
    assert radio is not None