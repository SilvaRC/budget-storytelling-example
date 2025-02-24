import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as mcolors
import os

def load_data(csv_file):
    """Loads data from a CSV file and returns a DataFrame."""
    df = pd.read_csv(csv_file, sep = ';')
    return df

def process_data(df):
    """Processes the DataFrame: computes log values and sorts by height."""
    df["percentage"] = df["Empenhado"]/np.sum(np.log(df["Empenhado"]))
    df["log_percentage"] = np.log(df["percentage"] * 100)
    df["empenhado_log"] = np.log(df["Empenhado"])

    df = df.sort_values(by="log_percentage", ascending=False)
    return df

#def get_bar_colors(values):
#    """Generates a color gradient from blue (smallest) to red (largest)."""
#    norm = mcolors.Normalize(vmin=min(values), vmax=max(values))  # Normalize values
#    cmap = cm.get_cmap("coolwarm")  # Use coolwarm colormap (red to blue)
#    return [cmap(norm(v)) for v in values]
    
def get_bar_colors(values, vmin=None, vmax=None):
    """Generates a color gradient from blue (smallest) to red (largest), with adjustable limits."""
    if vmin is None:
        vmin = min(values)  # Default to actual minimum
    if vmax is None:
        vmax = max(values)  # Default to actual maximum
    
    norm = mcolors.Normalize(vmin=vmin, vmax=vmax)  # Normalize values
    cmap = cm.get_cmap("coolwarm")  # Choose color palette (red to blue)
    return [cmap(norm(v)) for v in values]

def plot_histogram_percent_log(df):
    """Plots a histogram using Matplotlib with sorted values and formatted x-axis."""
    plt.figure(figsize=(12, 6))
    bars = plt.bar(df["Funcao"], df["log_percentage"], color="skyblue", edgecolor="black")
    
    # Get colors based on log values
    colors = get_bar_colors(df["log_percentage"])
        
    # Add value labels inside the bars
    for bar, value in zip(bars, df["log_percentage"]):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height()/2, 
                 f"{value:.2f}", ha='center', va='center', fontsize=8, color='black')
        
    plt.xlabel("Função", fontsize=12)
    plt.ylabel("Percentual (%) em escala logarítmica", fontsize=12)
    plt.title("Histograma do Percentual de Gastos por Função no Exercício 2015 (escala logarítmica)", fontsize=14)
    
    # Rotate x-axis labels for better readability
    plt.xticks(rotation=90, ha="right", fontsize=10)
    
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.show()

def plot_histogram_empenhado_log(df, output_folder):
    """Plots a histogram using Matplotlib with sorted values and formatted x-axis."""
    plt.figure(figsize=(12, 6))
    #bars = plt.bar(df["Funcao"], df["empenhado_log"], color="skyblue", edgecolor="black")
    
    # Get colors based on log values
    #colors = get_bar_colors(df["empenhado_log"]) 
    colors = get_bar_colors(df["empenhado_log"], vmin=0.5*min(df["empenhado_log"]), vmax=1.1*max(df["empenhado_log"]))  # Adjust limits
    
    bars = plt.bar(df["Funcao"], df["empenhado_log"], color=colors, edgecolor="black")    
    
    # Add value labels inside the bars
    for bar, value in zip(bars, df["Empenhado"]):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height()/2, 
                 f"R$ {(value/1000000000):.2f} bi", ha='center', va='center', fontsize=8, color='black', rotation=90)
        
    plt.xlabel("Função", fontsize=12)
    plt.ylabel("Valor empenhado (R$ bi) em escala logarítmica", fontsize=12)
    plt.title("Histograma dos Gastos por Função no Exercício 2015 (escala logarítmica)", fontsize=14)
    
    # Rotate x-axis labels for better readability
    plt.xticks(rotation=90, ha="right", fontsize=10)
    plt.yticks([])  # Removes y-axis ticks

    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()
    
    # Save the figure to the output folder
    plt.savefig(os.path.join(output_folder, "plot_histogram_empenhado_log.png"))
    
    plt.show()

def plot_histogram_empenhado(df, output_folder):
    """Plots a histogram using Matplotlib with sorted values and formatted x-axis."""
    plt.figure(figsize=(12, 6))
    #bars = plt.bar(df["Funcao"], df["empenhado_log"], color="skyblue", edgecolor="black")
    
    # Get colors based on log values
    #colors = get_bar_colors(df["empenhado_log"]) 
    colors = get_bar_colors(df["Empenhado"], vmin=0.5*min(df["Empenhado"]), vmax=1.1*max(df["Empenhado"]))  # Adjust limits
    
    bars = plt.bar(df["Funcao"], df["Empenhado"], color=colors, edgecolor="black")    
    
    # Add value labels inside the bars
    for bar, value in zip(bars, df["Empenhado"]):
        plt.text(bar.get_x() + bar.get_width(), bar.get_height()+100000000000, 
                 f"R$ {(value/1000000000):.2f} bi", ha='center', va='center', fontsize=8, color='black', rotation = 45)
        
    plt.xlabel("Função", fontsize=12)
    plt.ylabel("Valor empenhado (R$ bi)", fontsize=12)
    plt.title("Histograma dos Gastos por Função no Exercício 2015", fontsize=14)
    
    # Rotate x-axis labels for better readability
    plt.xticks(rotation=90, ha="right", fontsize=10)
    plt.yticks([])  # Removes y-axis ticks

    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()
    
    # Save the figure to the output folder
    plt.savefig(os.path.join(output_folder, "plot_histogram_empenhado.png"))
    
    plt.show()

def plot_histogram_empenhado_horiz(df, output_folder):
    """Plots a histogram using Matplotlib with sorted values and formatted x-axis."""
    plt.figure(figsize=(12, 6))
    #bars = plt.bar(df["Funcao"], df["empenhado_log"], color="skyblue", edgecolor="black")
    
    # Get colors based on log values
    #colors = get_bar_colors(df["empenhado_log"]) 
    colors = get_bar_colors(df["Empenhado"], vmin=0.5*min(df["Empenhado"]), vmax=1.1*max(df["Empenhado"]))  # Adjust limits
    
    df.sort_values(by="Empenhado", ascending=True)
    bars = plt.barh(df["Funcao"], df["Empenhado"], color=colors, edgecolor="black")    
    
    # Add value labels inside the bars
    for bar, value in zip(bars, df["Empenhado"]):
        plt.text(bar.get_width()/2, bar.get_y() + bar.get_height()/2 + 10000, 
                 f"R$ {(value/1000000000):.2f} bi", ha='center', va='center', fontsize=10, color='black')
                 
    plt.ylabel("Função", fontsize=12)
    plt.xlabel("Valor empenhado (R$ bi)", fontsize=12)
    plt.title("Histograma dos Gastos por Função no Exercício 2015", fontsize=14)
    
    # Rotate x-axis labels for better readability
    plt.yticks(rotation=45, ha="right", fontsize=10)
    plt.xticks([])  # Removes y-axis ticks

    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()
    
    
    # Save the figure to the output folder
    plt.savefig(os.path.join(output_folder, "plot_histogram_empenhado_horiz.png"))
    
    plt.show()


def main():
    """Main function to load, process, and visualize the data."""
    csv_file = "ExecucaoOrcamento2015.csv"  # Change this to the actual CSV file path
    df = load_data(csv_file)
    df = process_data(df)
    output_folder = "images"
    
    #plot_histogram_percent_log(df)
    plot_histogram_empenhado_log(df, output_folder)
    plot_histogram_empenhado(df, output_folder)
    #plot_histogram_empenhado_horiz(df, output_folder)


if __name__ == "__main__":
    main()
