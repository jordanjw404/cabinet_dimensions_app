def determine_parts(values, unit_type):
    if unit_type == "Base Unit":
        return [
            ("1", "Top", values['Width'] - 36, values['Depth'], 18),
            ("1", "Left End", values['Depth'], values['Height'] - values['Leg Height'], 18),
            ("1", "Right End", values['Depth'], values['Height'] - values['Leg Height'], 18),
            ("1", "Bottom", values['Width'] - 36, values['Depth'], 18),
            (str(values['Shelf Total']), "Shelves", values['Width'] - 37, values['Depth'], max(0, values['Void'] - values['Inset']))
        ]
    # Add logic for other unit types
    return []
