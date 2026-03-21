from pathlib import Path
import matplotlib.pyplot as plt


def disp_graph(h, save=None, layout='spring', vertex_size=300, seed=42):
    """Display or save a plot of a Sage ``Graph`` object.

    Parameters:
        h: Sage Graph
        save: None or path-like. If provided, save the plot to this filename (PNG).
        layout: layout name for networkx (`spring`, `circular`, `kamada_kawai`) or a pos dict.
        vertex_size: size for nodes in Matplotlib drawing.
        seed: random seed for deterministic layouts (when layout is spring).

    Returns:
        path to saved file if save provided, else None.
    """
    try:
        # Convert to networkx for consistent drawing control
        Gnx = h.to_networkx()
    except Exception:
        # Fall back to Sage plotting if conversion fails
        P = h.plot(layout=layout, vertex_size=30, vertex_labels=True)
        if save:
            P.save(str(save))
            return Path(save).absolute()
        else:
            P.show()
            return None

    # choose position
    if isinstance(layout, dict):
        pos = layout
    elif layout == 'spring':
        import networkx as nx
        pos = nx.spring_layout(Gnx, seed=seed)
    elif layout == 'circular':
        import networkx as nx
        pos = nx.circular_layout(Gnx)
    elif layout == 'kamada_kawai':
        import networkx as nx
        pos = nx.kamada_kawai_layout(Gnx)
    else:
        import networkx as nx
        pos = nx.spring_layout(Gnx, seed=seed)

    import networkx as nx
    plt.figure(figsize=(6,6))
    nx.draw(Gnx, pos,
            with_labels=True,
            node_size=vertex_size,
            node_color='lightblue',
            edge_color='gray',
            font_size=10)
    plt.axis('off')
    if save:
        Path(save).parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(str(save), bbox_inches='tight', dpi=150)
        plt.close()
        return Path(save).absolute()
    else:
        plt.show()
        return None

def print_graph(h) :
    # helper to display a graph — define before using it
    print("vertice : ", h.vertices())
    print("Edges : ", h.edges(labels=False))
    h_spectrum = sorted([float(x) for x in h.spectrum()])
    print('Spectrum (rounded):', [float('{:.4f}'.format(x)) for x in h_spectrum])
