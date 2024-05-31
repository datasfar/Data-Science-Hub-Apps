import reflex as rx
import library_hub.styles.styles as styles

def card_3d() -> rx.Component:
    return rx.box( 
        rx.script(src="js/3d_card.js"),
        rx.html('''
        <div class="card">
            3D Card
            <div class="glow" />
        </div>
        ''')
    )

# Carga el js pero no consigo que carge el css desde stylesheets en @app