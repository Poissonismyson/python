def spaceCraft(navicelle):
        dic = {}
        dark_side = []
        light_side = []

        for entry in navicelle:
                data = entry.split(',')

                if data[0] == 'Lato Oscuro':
                        dark_side.append(data)
                else:
                        light_side.append(data)
        
        dark_side_sorted = sorted(dark_side, key = lambda x: int(x[3]), reverse=True)
        light_side_sorted = sorted(light_side, key = lambda x: int(x[3]), reverse=True)

        dark_side_final = [(i[2],i[1]) for i in dark_side_sorted]
        light_side_final = [(i[2],i[1]) for i in light_side_sorted]

        if dark_side_final:
                dic['Lato Oscuro'] = dark_side_final
        
        if light_side_final:
                dic['Lato Chiaro'] = light_side_final

        return dic
        
        
