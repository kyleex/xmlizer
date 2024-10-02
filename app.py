import streamlit as st
import xml.etree.ElementTree as ET
import docx

def docx_to_xml(docx_file):
    # Charger le fichier DOCX
    doc = docx.Document(docx_file)

    # Créer la racine du fichier XML
    root = ET.Element("document")

    # Lire chaque paragraphe du document DOCX
    for i, paragraph in enumerate(doc.paragraphs, 1):
        if paragraph.style.name.startswith('Heading'):
            heading_element = ET.SubElement(root, "title", level=paragraph.style.name)
            heading_element.text = paragraph.text
        else:
            para_element = ET.SubElement(root, "paragraph", id=str(i))
            para_element.text = paragraph.text

    # Retourner l'arbre XML sous forme de chaîne de caractères
    return ET.tostring(root, encoding="unicode", xml_declaration=True)

# Interface Streamlit
st.title("Convertisseur DOCX vers XML")

# Upload du fichier DOCX
uploaded_file = st.file_uploader("Téléchargez un fichier DOCX", type="docx")

if uploaded_file is not None:
    # Conversion du fichier DOCX en XML
    xml_output = docx_to_xml(uploaded_file)

    # Afficher le résultat XML
    st.text_area("XML généré :", value=xml_output, height=300)

    # Télécharger le fichier XML
    st.download_button(label="Télécharger le fichier XML", data=xml_output, file_name="document.xml", mime="application/xml")
