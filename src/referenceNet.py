import json
import networkx as nx
import matplotlib.pyplot as plt
import pydot
from networkx.drawing.nx_pydot import graphviz_layout
from pyvis.network import Network

class NetworkVisualizer:
    def __init__(self, data):
        self.data = data
        
    def make_graph(self, figsize = (15, 15), node_size = 800, font_size = 10, node_color='skyblue',
                   node_font_color='black', node_font_weight='bold', transparency=0.85,
                   connectionstyle="arc3, rad=0.08", label_font_color = 'red', label_font_size ='font_size',
                   output_name = '.\\output\\schema_blocchi.png'):    
        # Crea un grafo
        self.G = nx.DiGraph()

        # Aggiungi i nodi (blocchi)
        for item in self.data:
            risorsa = item['risorsa']
            self.G.add_node(risorsa)

            # Aggiungi archi (frecce) dalle chiavi di "reference" ai nodi
            reference = item['reference']
            if reference:
                for key, value in reference.items():
                    self.G.add_edge(risorsa, value, label=key)

        # Imposta il direzionamento del grafico
        self.G.graph['graph'] = {'rankdir': 'TB'}

        # Usa il layout di Graphviz
        pos = graphviz_layout(self.G, prog='dot')

        # Imposta il rapporto d'aspetto per rendere il grafico più grande
        fig, ax = plt.subplots(figsize=figsize)

        # Etichette rosse e allineate in orizzontale
        edge_labels = {edge: key for edge, key in nx.get_edge_attributes(self.G, 'label').items()}        

        # Modifica la dimensione e il colore delle etichette dei collegamenti
        label_font = {'color': label_font_color, 'font_size': label_font_size}

        # Draw graph
        nx.draw(self.G, pos, with_labels=True, node_size=node_size, node_color=node_color, 
                font_size=font_size, font_color=node_font_color, font_weight=node_font_weight, 
                labels={node: node for node in self.G.nodes()}, ax=ax, alpha=transparency,
                connectionstyle=connectionstyle)
        nx.draw_networkx_edge_labels(self.G, pos, edge_labels=edge_labels, 
                                    font_color='red', font_size=8, 
                                    label_pos=0.6, horizontalalignment='center', 
                                    verticalalignment='center', rotate=False,
                                    clip_on=False)

        # Salva il grafico come immagine
        plt.savefig(output_name, format='png', bbox_inches='tight')

        # Mostra il grafico
        #plt.show()

    def make_html_plot(self, output_name = '.\\output\\mygraph.html'):
        # creat vis network
        net = Network(notebook=False) # Set notebook=False to generate a standalone HTML, True for JupyterNotebook
        # load the network graph 
        net.from_nx(self.G)
        # Save the graph as an HTML file
        net.toggle_physics(True)
        net.show_buttons(filter_=['physics'])
        net.show(output_name,notebook=False)
    
    def make_pyvis_network(self, output_name = '.\\output\\mygraph.html'):
        # Create a Pyvis network
        net = Network(notebook=False, bgcolor='white')#,heading="Visualize FHIR message reference")#, layout=True)

        # Add nodes to the Pyvis network
        for node in self.G.nodes:
            label = f'<b>{node}</b>'  # Wrap the label in <b> tags for bold formatting
            if node == "MessageHeader":
                color='forestgreen'
                net.add_node(node, title=label, font={'color': 'green'}, color = color, borderWidth=10,
                             borderWidthSelected = 2, mass = 2.5)  
            else: 
                net.add_node(node, title=label, font={'color': 'red'}, mass = 2)#, color = color, borderWidth=10)  
            
        # Add edges to the Pyvis network with arrows
        for edge in self.G.edges(data=True):
            source, target, data = edge
            label = data['label']
            # Use the 'to' property to add arrows to the edge
            net.add_edge(source, target, label=label, arrows='to', color='black') 

        # Set physics options (not working now)
        physics_options = {
            "forceAtlas2Based": {
                "gravitationalConstant": -91,
                "springLength": 100,
                "springConstant": 0.11,
                "damping": 0.47,
                "avoidOverlap": 0.1
            },
            "minVelocity": 0.75,
            "solver": "forceAtlas2Based"
        }
    
        # Convert the physics options to a JSON string
        physics_options_json = json.dumps(physics_options)

        # Create a dictionary with the expected structure
        formatted_options = {
            "physics": {
                "enabled": True,
                "options": physics_options_json
            }
        }

        # Now you can pass formatted_options to the toggle_physics function
        #net.toggle_physics(formatted_options)
        net.toggle_physics(True)

        net.show_buttons(filter_=['physics'])
        net.show(output_name,notebook=False)