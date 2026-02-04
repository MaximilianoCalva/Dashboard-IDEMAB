import os

# Configuration
output_dir = "Dashboard/TarotTerapeutico"
modules = [f"M{i}" for i in range(1, 7)] # 6 Modules
# PLACEHOLDER - USER MUST UPDATE THIS
api_placeholder = "https://script.google.com/macros/s/AKfycbzrHUZHc1yW5sG_pBQtLRim6i5KetHAImyWY6Vga1ib80EyNkKNo87JSHn1B332cHogSQ/exec"

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

# Templates
template_aula = """
<!-- Snippet: Aula TV {module} - Tarot Terapeutico -->
<script src="https://cdn.tailwindcss.com"></script>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&family=Inter:wght@300;400;500&display=swap" rel="stylesheet">
<style> 
    .idemab-font-title {{ font-family: 'Outfit', sans-serif; }}
    .idemab-font-body {{ font-family: 'Inter', sans-serif; }}
    .glass-card {{
        background: white;
        border: 1px solid rgba(229, 231, 235, 0.5);
    }}
</style>

<div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
    <!-- Header -->
    <div class="mb-12 border-l-4 border-purple-600 pl-6">
        <h2 class="text-4xl font-bold text-gray-900 idemab-font-title tracking-tight mb-2">Módulo {module_num}</h2>
        <p class="text-lg text-gray-500 idemab-font-body">Diplomado en Tarot Terapéutico</p>
    </div>

    <!-- Skeleton Loader -->
    <div id="loading-aula-{module}" class="space-y-8">
        <!-- 2 Skeletons -->
        <div class="bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden">
            <div class="aspect-video bg-gray-100 animate-pulse"></div>
            <div class="p-6 space-y-3">
                <div class="h-6 bg-gray-100 rounded w-1/3 animate-pulse"></div>
                <div class="h-4 bg-gray-100 rounded w-3/4 animate-pulse"></div>
            </div>
        </div>
        <div class="bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden">
            <div class="aspect-video bg-gray-100 animate-pulse"></div>
            <div class="p-6 space-y-3">
                <div class="h-6 bg-gray-100 rounded w-1/3 animate-pulse"></div>
                <div class="h-4 bg-gray-100 rounded w-3/4 animate-pulse"></div>
            </div>
        </div>
    </div>

    <!-- Content Stack -->
    <div id="aula-grid-{module}" class="flex flex-col gap-12 hidden opacity-0 transition-opacity duration-700">
        <!-- Cards injected here -->
    </div>
    
    <div id="error-msg-{module}" class="hidden text-center bg-red-50 text-red-600 p-4 rounded-lg mt-4"></div>
</div>

<script>
    (function() {{
        const API_URL = '{api_url}';
        const TAB_PREFIX = 'Aula TV {module}';
        const GRID_ID = 'aula-grid-{module}';
        const LOAD_ID = 'loading-aula-{module}';
        const ERR_ID = 'error-msg-{module}';

        function getEmbedUrl(link) {{
            if (!link) return null;
            if (link.includes('youtube.com') || link.includes('youtu.be')) {{
                let vid = '';
                try {{
                    vid = link.includes('v=') ? link.split('v=')[1].split('&')[0] : link.split('/').pop();
                    return `https://www.youtube.com/embed/${{vid}}`;
                }} catch(e) {{ return null; }}
            }}
            if (link.includes('vimeo.com')) {{
                try {{
                    const vid = link.split('/').pop().split('?')[0];
                    return `https://player.vimeo.com/video/${{vid}}`;
                }} catch(e) {{ return null; }}
            }}
            return null;
        }}

        async function load() {{
            const grid = document.getElementById(GRID_ID);
            const loader = document.getElementById(LOAD_ID);
            const errorDiv = document.getElementById(ERR_ID);

            try {{
                const res = await fetch(API_URL);
                const allData = await res.json();
                const exactKey = Object.keys(allData).find(k => k.trim().startsWith(TAB_PREFIX));
                const items = exactKey ? allData[exactKey] : [];
                
                if (items.length === 0) {{
                    grid.innerHTML = `
                        <div class="text-center py-16 bg-gray-50 rounded-3xl border border-dashed border-gray-200">
                            <p class="text-gray-400 idemab-font-body">No hay lecciones disponibles.</p>
                        </div>`;
                }} else {{
                    grid.innerHTML = items.map((item, index) => {{
                        if (item.status && String(item.status).toLowerCase().includes('inactivo')) return '';
                        
                        const embedUrl = getEmbedUrl(item.link);
                        let mediaContent = '';

                        if (embedUrl) {{
                            mediaContent = `
                                <div class="relative w-full aspect-video bg-black shadow-inner">
                                    <iframe src="${{embedUrl}}" class="absolute inset-0 w-full h-full" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
                                </div>
                            `;
                        }} else {{
                            mediaContent = `
                                <div class="h-64 bg-gray-900 flex flex-col items-center justify-center text-gray-500">
                                    <svg class="w-16 h-16 mb-2 opacity-50" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M14.752 11.168l-3.197-2.132A1 1 0 0010 9.87v4.263a1 1 0 001.555.832l3.197-2.132a1 1 0 000-1.664z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                                    <span class="text-sm font-medium">Video no disponible</span>
                                </div>
                            `;
                        }}

                        return `
                        <article class="bg-white rounded-3xl shadow-xl shadow-gray-100 overflow-hidden border border-gray-100 flex flex-col">
                            <!-- Video Section -->
                            ${{mediaContent}}
                            
                            <!-- Info Section -->
                            <div class="p-8">
                                <div class="flex items-center gap-3 mb-4">
                                    <span class="flex items-center justify-center w-8 h-8 rounded-full bg-purple-100 text-purple-700 text-sm font-bold idemab-font-title">
                                        ${{index + 1}}
                                    </span>
                                    <h3 class="text-2xl font-bold text-gray-900 idemab-font-title leading-tight">${{item.titulo}}</h3>
                                </div>
                                <div class="pl-11">
                                    <p class="text-gray-600 idemab-font-body leading-relaxed text-lg">${{item.descripcion || 'Sin descripción.'}}</p>
                                    <div class="pt-4 mt-6 border-t border-gray-100 flex items-center justify-between">
                                        <div class="flex items-center gap-2">
                                            <span class="w-2 h-2 rounded-full bg-red-500 animate-pulse"></span>
                                            <span class="text-xs font-medium text-gray-500 uppercase tracking-wide">Video Player</span>
                                        </div>
                                        <span class="text-xs font-bold text-gray-400 bg-gray-50 px-2 py-1 rounded">Aula TV</span>
                                    </div>
                                </div>
                            </div>
                        </article>`;
                    }}).join('');
                }}
                
                grid.classList.remove('hidden');
                setTimeout(() => {{ grid.classList.remove('opacity-0'); }}, 100);

            }} catch (e) {{
                errorDiv.innerHTML = `<p class="text-red-500 font-medium">Error: ${{e.message}}</p>`;
                errorDiv.classList.remove('hidden');
            }} finally {{
                loader.classList.add('hidden');
            }}
        }}

        document.addEventListener('DOMContentLoaded', load);
    }})();
</script>
"""

template_material = """
<!-- Snippet: Material {module} - Tarot Terapeutico -->
<script src="https://cdn.tailwindcss.com"></script>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style> .idemab-material {{ font-family: 'Inter', sans-serif; }} </style>

<div class="idemab-material max-w-7xl mx-auto p-4">
    <div class="text-center mb-8">
        <h2 class="text-2xl font-bold text-gray-800 tracking-tight">Material - Módulo {module_num}</h2>
        <p class="text-gray-500 mt-1">Recursos del Módulo {module_num} (Diplomado en Tarot Terapéutico)</p>
    </div>

    <div id="loading-mat-{module}" class="text-center py-10">
        <div class="animate-spin rounded-full h-10 w-10 border-b-2 border-blue-600 mx-auto"></div>
        <p class="text-gray-400 text-sm mt-3">Cargando material...</p>
    </div>

    <div id="list-mat-{module}" class="grid grid-cols-1 gap-4 hidden max-w-4xl mx-auto">
        <!-- Items injected here -->
    </div>
    
    <div id="error-mat-{module}" class="hidden text-center text-red-500 py-4"></div>
</div>

<script>
    (function() {{
        const API_URL = '{api_url}';
        const TAB_PREFIX = 'Material {module}'; // Prefix to search for
        const LIST_ID = 'list-mat-{module}';
        const LOAD_ID = 'loading-mat-{module}';
        const ERR_ID = 'error-mat-{module}';

        async function load() {{
            const list = document.getElementById(LIST_ID);
            const loader = document.getElementById(LOAD_ID);
            const errorDiv = document.getElementById(ERR_ID);

            try {{
                const res = await fetch(API_URL);
                const allData = await res.json();
                
                // Fuzzy Match
                const exactKey = Object.keys(allData).find(k => k.trim().startsWith(TAB_PREFIX));
                const items = exactKey ? allData[exactKey] : [];
                
                if (items.length === 0) {{
                    list.innerHTML = '<p class="text-center text-gray-400">No hay materiales disponibles.</p>';
                }} else {{
                    list.innerHTML = items.map(item => {{
                        if (item.status && String(item.status).toLowerCase().includes('inactivo')) return '';
                        
                        let icon = '<svg class="w-6 h-6 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 21h10a2 2 0 002-2V9.414a1 1 0 00-.293-.707l-5.414-5.414A1 1 0 0012.586 3H7a2 2 0 00-2 2v14a2 2 0 002 2z" /></svg>';
                        if (item.formato && item.formato.toLowerCase().includes('pdf')) {{
                            icon = '<svg class="w-6 h-6 text-red-500" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 21h10a2 2 0 002-2V9.414a1 1 0 00-.293-.707l-5.414-5.414A1 1 0 0012.586 3H7a2 2 0 00-2 2v14a2 2 0 002 2z" /></svg>';
                        }}

                        return `
                        <div class="bg-white p-4 rounded-xl border border-gray-200 shadow-sm flex flex-col md:flex-row items-start md:items-center justify-between gap-4 hover:bg-gray-50 transition-colors">
                            <div class="flex items-start gap-4">
                                <div class="mt-1">${{icon}}</div>
                                <div>
                                    <h3 class="font-semibold text-gray-800">${{item.titulo}}</h3>
                                    <p class="text-sm text-gray-500">${{item.descripcion || ''}}</p>
                                </div>
                            </div>
                            <a href="${{item.link}}" target="_blank" class="px-4 py-2 bg-white border border-gray-300 rounded-lg text-sm font-medium text-gray-700 hover:bg-gray-50 hover:text-blue-600 transition-colors whitespace-nowrap">
                                Descargar
                            </a>
                        </div>`;
                    }}).join('');
                }}
                list.classList.remove('hidden');
            }} catch (e) {{
                errorDiv.innerHTML = `Error: ${{e.message}}`;
                errorDiv.classList.remove('hidden');
            }} finally {{
                loader.classList.add('hidden');
            }}
        }}

        document.addEventListener('DOMContentLoaded', load);
    }})();
</script>
"""

# Generate files
for mod in modules:
    mod_num = mod.replace('M', '')
    
    # Aula TV
    file_aula = f"{output_dir}/snippet-tarot-{mod.lower()}-aula-tv.html"
    with open(file_aula, "w", encoding="utf-8") as f:
        f.write(template_aula.format(module=mod, module_num=mod_num, api_url=api_placeholder))
    print(f"Generated: {file_aula}")

    # Material
    file_mat = f"{output_dir}/snippet-tarot-{mod.lower()}-material.html"
    with open(file_mat, "w", encoding="utf-8") as f:
        f.write(template_material.format(module=mod, module_num=mod_num, api_url=api_placeholder))
    print(f"Generated: {file_mat}")
