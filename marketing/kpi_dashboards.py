"""
KPI Dashboard — Portafolio Andrés Carrión
Visualización de métricas de éxito para los casos de estudio:
  1. Dominó x Doritos x NotCo (Comunicación Integral en Marketing)
  2. Aura Natural by Soprole (Branding)

Requiere: pip install matplotlib numpy
Genera: kpi_dashboard_caso1.png, kpi_dashboard_caso2.png
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# ─── Configuración global ───────────────────────────────────────────
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['DejaVu Sans'],
    'font.size': 11,
    'axes.spines.top': False,
    'axes.spines.right': False,
})

COLORS = {
    'primary': '#1a1a2e',
    'accent': '#e94560',
    'success': '#0f3460',
    'gold': '#c5a030',
    'light': '#f5f5f5',
    'green': '#2d6a4f',
    'sage': '#84a98c',
}


# ═══════════════════════════════════════════════════════════════════
# CASO 1: Dominó x Doritos x NotCo
# ═══════════════════════════════════════════════════════════════════

def create_caso1_dashboard():
    fig = plt.figure(figsize=(16, 10), facecolor='white')
    fig.suptitle('Dashboard KPIs — Alianza Dominó × Doritos × NotCo',
                 fontsize=18, fontweight='bold', color=COLORS['primary'], y=0.97)
    fig.text(0.5, 0.935, 'Comunicación Integral en Marketing | Campaña 60 días',
             ha='center', fontsize=11, color='#666', style='italic')

    # ── Panel 1: ROI Proyectado (Gauge) ──
    ax1 = fig.add_subplot(2, 3, 1)
    roi_values = [1.0, 1.5, 2.2, 3.0]
    roi_labels = ['Break-even', 'Conservador', 'Optimista', 'Máx.']
    colors_roi = ['#ccc', COLORS['success'], COLORS['accent'], '#eee']
    
    theta = np.linspace(np.pi, 0, 100)
    for i in range(3):
        start = np.pi * (1 - roi_values[i]/3.0)
        end = np.pi * (1 - roi_values[i+1]/3.0)
        t = np.linspace(np.pi * (1 - roi_values[i]/3.0), np.pi * (1 - roi_values[i+1]/3.0), 50)
        ax1.fill_between(np.cos(t), np.sin(t)*0.6, np.sin(t)*0.9, 
                         color=colors_roi[i], alpha=0.7)
    
    # Needle at 1.85x (midpoint estimate)
    needle_angle = np.pi * (1 - 1.85/3.0)
    ax1.annotate('', xy=(np.cos(needle_angle)*0.75, np.sin(needle_angle)*0.75*0.6),
                xytext=(0, -0.05),
                arrowprops=dict(arrowstyle='->', color=COLORS['primary'], lw=2.5))
    ax1.text(0, -0.2, '1.85x', fontsize=20, fontweight='bold', ha='center', color=COLORS['accent'])
    ax1.text(0, -0.35, 'ROI Estimado', fontsize=10, ha='center', color='#666')
    ax1.set_xlim(-1.2, 1.2)
    ax1.set_ylim(-0.5, 1.1)
    ax1.axis('off')
    ax1.set_title('ROI Proyectado', fontsize=12, fontweight='bold', pad=10)

    # ── Panel 2: Trial Rate Objetivo ──
    ax2 = fig.add_subplot(2, 3, 2)
    categories = ['Semana\n1-2', 'Semana\n3-4', 'Semana\n5-6', 'Semana\n7-8']
    trial_proj = [3.5, 8.0, 12.5, 16.0]
    target_line = [15] * 4
    
    bars = ax2.bar(categories, trial_proj, color=COLORS['accent'], alpha=0.85, width=0.5, 
                   edgecolor='white', linewidth=1)
    ax2.plot(categories, target_line, '--', color=COLORS['success'], linewidth=2, label='Meta: 15%')
    ax2.set_ylabel('% del target alcanzado')
    ax2.set_title('Trial Rate Acumulado', fontsize=12, fontweight='bold', pad=10)
    ax2.legend(loc='upper left', fontsize=9)
    ax2.set_ylim(0, 20)
    for bar, val in zip(bars, trial_proj):
        ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.4,
                f'{val}%', ha='center', fontsize=9, fontweight='bold')

    # ── Panel 3: Share of Voice ──
    ax3 = fig.add_subplot(2, 3, 3)
    brands = ['Dominó×\nDoritos', "McDonald's", 'Burger\nKing', 'PJD', 'Otros']
    sov = [28, 22, 18, 12, 20]
    colors_sov = [COLORS['accent'], '#999', '#aaa', '#bbb', '#ddd']
    explode = (0.08, 0, 0, 0, 0)
    
    wedges, texts, autotexts = ax3.pie(sov, labels=brands, autopct='%1.0f%%',
                                        colors=colors_sov, explode=explode,
                                        textprops={'fontsize': 9},
                                        pctdistance=0.75)
    autotexts[0].set_fontweight('bold')
    autotexts[0].set_color('white')
    ax3.set_title('Share of Voice RRSS\n(Proyección Lanzamiento)', fontsize=12, fontweight='bold', pad=10)

    # ── Panel 4: Margen por Unidad ──
    ax4 = fig.add_subplot(2, 3, 4)
    components = ['Precio\nVenta', 'COGS\nBase', 'Costo\nDoritos/NotMayo', 'Margen\nContribución']
    values = [4500, -2200, -450, 1850]
    colors_bar = [COLORS['success'], COLORS['primary'], COLORS['primary'], COLORS['accent']]
    
    bars4 = ax4.barh(components, [abs(v) for v in values], color=colors_bar, alpha=0.85, height=0.5)
    for bar, val in zip(bars4, values):
        prefix = '-' if val < 0 else ''
        ax4.text(bar.get_width() + 50, bar.get_y() + bar.get_height()/2,
                f'{prefix}${abs(val):,} CLP', ha='left', va='center', fontsize=9, fontweight='bold')
    ax4.set_xlabel('CLP por unidad')
    ax4.set_title('Waterfall: Margen por Unidad', fontsize=12, fontweight='bold', pad=10)
    ax4.set_xlim(0, 5500)

    # ── Panel 5: Matriz de Riesgos ──
    ax5 = fig.add_subplot(2, 3, 5)
    risks = {
        'Canibalización': (0.5, 0.5),
        'Quiebre stock': (0.65, 0.85),
        'Percepción\ngimmick': (0.5, 0.8),
        'Fatiga ed.\nlimitada': (0.3, 0.45),
        'Conflicto\nmarca': (0.25, 0.5),
    }
    
    ax5.axhspan(0.66, 1.0, alpha=0.08, color='red')
    ax5.axhspan(0.33, 0.66, alpha=0.08, color='orange')
    ax5.axhspan(0.0, 0.33, alpha=0.08, color='green')
    
    for name, (prob, impact) in risks.items():
        size = prob * impact * 600 + 80
        ax5.scatter(prob, impact, s=size, alpha=0.7, color=COLORS['accent'], edgecolors=COLORS['primary'], linewidth=1)
        ax5.annotate(name, (prob, impact), fontsize=7.5, ha='center', va='bottom',
                    xytext=(0, 12), textcoords='offset points')
    
    ax5.set_xlabel('Probabilidad →')
    ax5.set_ylabel('Impacto →')
    ax5.set_xlim(0, 1)
    ax5.set_ylim(0, 1)
    ax5.set_title('Mapa de Riesgos', fontsize=12, fontweight='bold', pad=10)

    # ── Panel 6: NPS Target ──
    ax6 = fig.add_subplot(2, 3, 6)
    nps_categories = ['Detractores\n(0-6)', 'Pasivos\n(7-8)', 'Promotores\n(9-10)']
    nps_values = [15, 30, 55]
    nps_colors = ['#e74c3c', '#f39c12', COLORS['green']]
    
    bars6 = ax6.bar(nps_categories, nps_values, color=nps_colors, alpha=0.85, width=0.5,
                    edgecolor='white', linewidth=1)
    for bar, val in zip(bars6, nps_values):
        ax6.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                f'{val}%', ha='center', fontsize=11, fontweight='bold')
    
    ax6.set_ylabel('% de encuestados')
    ax6.set_title(f'NPS Objetivo: +{nps_values[2] - nps_values[0]}', fontsize=12, fontweight='bold', pad=10)
    ax6.set_ylim(0, 70)

    plt.tight_layout(rect=[0, 0, 1, 0.92])
    plt.savefig('/home/claude/kpi_dashboard_caso1.png', dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print("✓ Dashboard Caso 1 generado")


# ═══════════════════════════════════════════════════════════════════
# CASO 2: Aura Natural by Soprole
# ═══════════════════════════════════════════════════════════════════

def create_caso2_dashboard():
    fig = plt.figure(figsize=(16, 10), facecolor='white')
    fig.suptitle('Dashboard KPIs — Aura Natural, por Soprole',
                 fontsize=18, fontweight='bold', color=COLORS['green'], y=0.97)
    fig.text(0.5, 0.935, 'Branding | Estrategia de Desarrollo de Producto (Ansoff)',
             ha='center', fontsize=11, color='#666', style='italic')

    # ── Panel 1: Estructura de Costos ──
    ax1 = fig.add_subplot(2, 3, 1)
    cost_items = ['Envase\nvidrio', 'Ingredientes\npremium', 'Producción\n+ logística', 'Margen\nbruto']
    cost_values = [315, 250, 185, 1240]
    cost_pct = [f'{v/1990*100:.0f}%' for v in cost_values]
    cost_colors = [COLORS['primary'], COLORS['sage'], '#999', COLORS['green']]
    
    bars1 = ax1.bar(cost_items, cost_values, color=cost_colors, alpha=0.85, width=0.55,
                    edgecolor='white', linewidth=1)
    for bar, val, pct in zip(bars1, cost_values, cost_pct):
        ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 20,
                f'${val}\n({pct})', ha='center', fontsize=9, fontweight='bold')
    ax1.set_ylabel('CLP por unidad')
    ax1.set_title('Estructura de Costos\n(PVP: $1.990)', fontsize=12, fontweight='bold', pad=10)
    ax1.set_ylim(0, 1500)

    # ── Panel 2: Break-even Analysis ──
    ax2 = fig.add_subplot(2, 3, 2)
    months = np.arange(1, 13)
    revenue_cum = np.array([8, 18, 32, 48, 68, 90, 115, 142, 170, 200, 232, 265])
    cost_cum = np.array([150, 155, 162, 170, 180, 192, 205, 218, 232, 247, 262, 278])
    
    ax2.plot(months, revenue_cum, '-o', color=COLORS['green'], linewidth=2, markersize=5, label='Ingreso acumulado')
    ax2.plot(months, cost_cum, '--s', color=COLORS['accent'], linewidth=2, markersize=5, label='Costo acumulado')
    ax2.fill_between(months, revenue_cum, cost_cum, 
                     where=(revenue_cum >= cost_cum), alpha=0.15, color=COLORS['green'])
    ax2.fill_between(months, revenue_cum, cost_cum,
                     where=(revenue_cum < cost_cum), alpha=0.15, color=COLORS['accent'])
    
    # Mark break-even
    ax2.axvline(x=7.5, color=COLORS['gold'], linestyle=':', linewidth=2)
    ax2.annotate('Break-even\n~Mes 7-8', xy=(7.5, 210), fontsize=9, fontweight='bold',
                color=COLORS['gold'], ha='center')
    
    ax2.set_xlabel('Mes')
    ax2.set_ylabel('$M CLP (acumulado)')
    ax2.set_title('Análisis de Break-even', fontsize=12, fontweight='bold', pad=10)
    ax2.legend(fontsize=9)
    ax2.set_xticks(months)

    # ── Panel 3: Market Share Objetivo ──
    ax3 = fig.add_subplot(2, 3, 3)
    segments = ['Soprole\nBase', 'Colún', 'Nestlé', 'Danone', 'Artesanales\n/ Nicho', 'AURA\nNATURAL']
    shares = [28, 22, 18, 12, 18, 2]
    seg_colors = ['#ccc', '#bbb', '#aaa', '#999', '#888', COLORS['green']]
    
    wedges, texts, autotexts = ax3.pie(shares, labels=segments, autopct='%1.0f%%',
                                        colors=seg_colors,
                                        explode=(0, 0, 0, 0, 0, 0.12),
                                        textprops={'fontsize': 8.5},
                                        pctdistance=0.78)
    autotexts[-1].set_fontweight('bold')
    autotexts[-1].set_color('white')
    ax3.set_title('Market Share Lácteos Premium\n(Objetivo Año 1)', fontsize=12, fontweight='bold', pad=10)

    # ── Panel 4: Atención Visual (IA) ──
    ax4 = fig.add_subplot(2, 3, 4)
    elements = ['Logo\n"Aura Natural"', 'Respaldo\n"por Soprole"', 'Beneficios\nfuncionales', 'Ilustraciones\nbotánicas']
    before = [24.9, 8.9, 29.3, 0.7]
    after = [29.0, 14.8, 34.6, 3.2]
    
    x = np.arange(len(elements))
    w = 0.3
    bars_b = ax4.bar(x - w/2, before, w, label='Diseño Original', color='#ccc', edgecolor='white')
    bars_a = ax4.bar(x + w/2, after, w, label='Diseño Optimizado', color=COLORS['green'], 
                     alpha=0.85, edgecolor='white')
    
    for bar, val in zip(bars_a, after):
        ax4.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                f'{val}%', ha='center', fontsize=8.5, fontweight='bold', color=COLORS['green'])
    
    ax4.set_ylabel('% Atención Visual')
    ax4.set_title('A/B Testing: Mapa de Calor IA', fontsize=12, fontweight='bold', pad=10)
    ax4.set_xticks(x)
    ax4.set_xticklabels(elements, fontsize=8.5)
    ax4.legend(fontsize=9)
    ax4.set_ylim(0, 42)

    # ── Panel 5: Tasa de Recompra Proyectada ──
    ax5 = fig.add_subplot(2, 3, 5)
    quarters = ['Q1', 'Q2', 'Q3', 'Q4']
    recompra = [18, 28, 33, 38]
    target_rep = [35] * 4
    
    ax5.plot(quarters, recompra, '-o', color=COLORS['green'], linewidth=2.5, markersize=8)
    ax5.plot(quarters, target_rep, '--', color=COLORS['gold'], linewidth=2, label='Meta: 35%')
    ax5.fill_between(quarters, recompra, alpha=0.1, color=COLORS['green'])
    
    for q, val in zip(quarters, recompra):
        ax5.text(q, val + 1.5, f'{val}%', ha='center', fontsize=10, fontweight='bold')
    
    ax5.set_ylabel('% de recompra (90 días)')
    ax5.set_title('Tasa de Recompra Proyectada', fontsize=12, fontweight='bold', pad=10)
    ax5.legend(fontsize=9)
    ax5.set_ylim(0, 50)

    # ── Panel 6: NPS Benchmark ──
    ax6 = fig.add_subplot(2, 3, 6)
    brands_nps = ['Soprole\nBase', 'Colún', 'Danone', 'Artesanales', 'AURA\nNATURAL\n(objetivo)']
    nps_scores = [32, 38, 28, 55, 50]
    nps_bar_colors = ['#ccc', '#bbb', '#aaa', '#999', COLORS['green']]
    
    bars6 = ax6.barh(brands_nps, nps_scores, color=nps_bar_colors, alpha=0.85, height=0.5,
                     edgecolor='white', linewidth=1)
    for bar, val in zip(bars6, nps_scores):
        ax6.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2,
                f'+{val}', ha='left', va='center', fontsize=10, fontweight='bold')
    ax6.set_xlabel('NPS Score')
    ax6.set_title('NPS Benchmark vs. Competencia', fontsize=12, fontweight='bold', pad=10)
    ax6.set_xlim(0, 70)

    plt.tight_layout(rect=[0, 0, 1, 0.92])
    plt.savefig('/home/claude/kpi_dashboard_caso2.png', dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print("✓ Dashboard Caso 2 generado")


# ═══════════════════════════════════════════════════════════════════
if __name__ == '__main__':
    create_caso1_dashboard()
    create_caso2_dashboard()
    print("\n✅ Ambos dashboards generados exitosamente.")
