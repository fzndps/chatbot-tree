class Node:
    def __init__(self, question, yes_node=None, no_node=None, hasil=None):
        self.question = question
        self.yes_node = yes_node
        self.no_node = no_node
        self.hasil = hasil


    def build_tree():

        # Hasil akhir spesifikasi untuk setiap simpul akhir
        miskin = Node(None, hasil="Kalo miskin jangan rakit PC, anjing")

        server1 = Node(None, hasil="""   \nRekomendasi PC Server Entry-Level (<10 juta):
Processor: Intel Xeon E-2224G
Motherboard: Server Board Entry (C242 chipset)
RAM: 16GB DDR4 ECC
Storage: SSD 512GB + HDD 2TB
PSU: 500W 80+ Bronze
Casing: Rackmount 1U Server Case""")

        server2 = Node(None, hasil="""   \nRekomendasi PC Server Mid-Level (10-20 juta):
Processor: AMD EPYC 7232P
Motherboard: Server Board (Socket SP3)
RAM: 32GB DDR4 ECC
Storage: SSD NVMe 1TB + HDD 4TB
PSU: 650W 80+ Gold
Casing: Rackmount 2U Server Case""")

        server3 = Node(None, hasil="""   \nRekomendasi PC Server High-End (>20 juta):
Processor: Intel Xeon Silver 4310
Motherboard: Server Board (C620 chipset)
RAM: 64GB DDR4 ECC
Storage: SSD NVMe 2TB + HDD 8TB
PSU: 750W 80+ Platinum
Casing: Rackmount 4U Server Case""")

        
        entry2 = Node(None, hasil="""   \nRekomendasi PC Entry-Level (<7 juta) AMD:
                      
Processor: AMD Ryzen 5 5600G (APU untuk efisiensi).
Motherboard: B450
RAM: 16GB DDR4 3200 MHz
Storage: SSD NVMe 512GB
PSU: 450W 80+ Bronze
Casing: Aerocool Aero One.""")
        
        entry1 = Node(None, hasil="""   \nRekomendasi PC Entry-Level (<7 juta) Intel:

Intel:
Processor: Intel Core i3-12100F
Motherboard: H610
RAM: 16GB DDR4 3200 MHz
Storage: SSD NVMe 512GB
VGA: Integrated GPU
PSU: 450W 80+ Bronze
Casing: Cooler Master MasterBox Lite.""")
        
        mid2 = Node(None, hasil="""     \nRekomendasi PC High-End (>15 juta) Intel:
                    
AMD:
Processor: AMD Ryzen 5 7600
Motherboard: B650
RAM: 16GB DDR5 5200 MHz
Storage: SSD NVMe 1TB
VGA: AMD RX 6600 XT
PSU: 550W 80+ Bronze
Casing: Thermaltake Versa J23.""")
        
        mid1 = Node(None, hasil="""     \nRekomendasi PC High-End (>15 juta) Intel:

Intel:
Processor: Intel Core i5-13400F
Motherboard: B760
RAM: 16GB DDR5 4800 MHz
Storage: SSD NVMe 1TB
VGA: NVIDIA GTX 1660 Ti
PSU: 550W 80+ Bronze
Casing: Deepcool Matrexx 55 Mesh.""")
        
        high4 = Node(None, hasil="""      \nRekomendasi PC High-End (>15 juta) Mac Studio
Chipset:
Apple M2 Max: CPU 12-core, GPU hingga 38-core.
Apple M2 Ultra: CPU 24-core, GPU hingga 76-core.

Memori & Penyimpanan:
RAM: Hingga 192GB (M2 Ultra).
Penyimpanan: SSD mulai dari 512GB hingga 8TB.

Port:
Thunderbolt 4 (4 port di belakang).
USB-A (2 port), HDMI, Ethernet hingga 10Gb.

Dimensi & Berat:
Tinggi: 3,7 inci (9,5 cm), Lebar: 7,7 inci (19,7 cm), Berat: Hingga 3,6 kg (M2 Ultra).

Kelebihan:
Dirancang untuk workflow profesional seperti pengeditan video 3D dan simulasi.
Lebih banyak opsi memori dan performa dibanding Mac Mini
APPLE SUPPORT MACRUMORS.
""")
        
        high3 = Node(None, hasil="""      \nRekomendasi PC High-End (>15 juta) Mac Mini
Chipset:
Apple M4: CPU 10-core, GPU hingga 16-core, dan Neural Engine 16-core.
Apple M4 Pro: CPU 14-core, GPU hingga 20-core, dan Neural Engine 16-core.

Memori & Penyimpanan:
RAM: Hingga 32GB (M4) atau 64GB (M4 Pro).
Penyimpanan: SSD mulai dari 512GB hingga 8TB.

Port:
Thunderbolt 4 (2-4 port, tergantung model).
HDMI, USB-A, Ethernet (hingga 10Gb).

Dimensi & Berat:
Tinggi: 2 inci (5 cm), Lebar: 5 inci (12,7 cm), Berat: ~0,7 kg.

Fitur Tambahan:
Konsumsi daya maksimum 155W.
Dukungan macOS terbaru dengan fitur iPhone Mirroring, window tiling, dll
APPLE SUPPORT MACRUMORS
""")
        
        high2 = Node(None, hasil="""      \nRekomendasi PC High-End (>15 juta) AMD:
                     
Processor: AMD Ryzen 7 7800X3D
Motherboard: B650 atau X670
RAM: 32GB DDR5 6000 MHz (dual-channel)
Storage: SSD NVMe 1TB + HDD 2TB
VGA: AMD RX 7800 XT atau NVIDIA RTX 4070
PSU: 650W 80+ Gold
Casing: Phanteks Eclipse P400A, Cooler Master TD500 Mesh, atau Fractal Design Meshify C.""")
        
        high1 = Node(None, hasil="""      \nRekomendasi PC High-End (>15 juta) Intel:
                     
Processor: Intel Core i5-14600K atau i7-13700F
Motherboard: Z790 atau B760
RAM: 32GB DDR5 5600 MHz (dual-channel)
Storage: SSD NVMe 1TB + HDD 2TB
VGA: NVIDIA RTX 4060 Ti atau RTX 4070
PSU: 650W 80+ Gold
Casing: NZXT H510 Elite, Lian Li Lancool II Mesh, atau Corsair 4000D Airflow.""")
        
        
        # Bangun simpul dari bawah ke atas
        pilihan_tidak_ada = Node(None, hasil="Mohon maaf pilihan tidak ada")
        
        pc_entry2 = Node("Apakah anda ingin menggunakan processor AMD?", yes_node=entry2, no_node=pilihan_tidak_ada)
        pc_entry1 = Node("Apakah anda ingin menggunakan processor INTEL?", yes_node=entry1, no_node=pc_entry2)

        pc_mid2 = Node("Apakah anda ingin menggunakan processor AMD?", yes_node=mid2, no_node=pilihan_tidak_ada)
        pc_mid1 = Node("Apakah anda ingin menggunakan processor INTEL?", yes_node=mid1, no_node=pc_mid2)

        pc_high4 = Node("Apakah anda ingin Mac studio?", yes_node=high4, no_node=pilihan_tidak_ada)
        pc_high3 = Node("Apakah anda ingin Mac mini?", yes_node=high3, no_node=pc_high4)
        pc_high2 = Node("Apakah anda ingin menggunakan processor AMD?", yes_node=high2, no_node=pc_high3)
        pc_high1 = Node("Apakah anda ingin menggunakan processor INTEL?", yes_node=high1, no_node=pc_high2)

        budget_tidak_ada = Node(None, hasil="Mohon maaf budget anda tidak mencukupi")
        budget3 = Node("Apakah budget Anda di atas 8 juta?", yes_node=pc_entry1, no_node=budget_tidak_ada)
        budget2 = Node("Apakah budget Anda antara 8-15 juta?", yes_node=pc_mid1, no_node=budget3)
        budget1 = Node("Apakah budget Anda di bawah 15 juta?", yes_node=pc_high1, no_node=budget2)
        
        game_tidak_ada = Node(None, hasil="Mohon maaf untuk genre game hanya sebatas itu")
        gaming3 = Node("Apakah Anda suka bermain game genre Casual?", yes_node=budget1, no_node=game_tidak_ada)
        gaming2 = Node("Apakah Anda suka bermain game genre eSport?", yes_node=budget1, no_node=gaming3)
        gaming1 = Node("Apakah Anda suka bermain game genre OpenWorld atau RPG?", yes_node=budget1, no_node=gaming2)
        
        tujuan_pc_tidak_ada = Node(None, hasil="Mohon maaf untuk pilihan hanya sebatas itu")
        
        pc_creator3 = Node("Apakah Anda ingin PC High-End untuk konten kreator game ringan dan editing sedikit?", yes_node=budget3, no_node=tujuan_pc_tidak_ada)
        pc_creator2 = Node("Apakah Anda ingin PC Mid-Level untuk konten kreator game menengah dan editing tipis live streaming?", yes_node=budget2, no_node=pc_creator3)
        pc_creator1 = Node("Apakah Anda ingin PC untuk konten kreator game berat dan editing dan live streaming?", yes_node=budget1, no_node=pc_creator2)
        
        pc_server3 = Node("Apakah Anda ingin server High-End?", yes_node=server3, no_node=tujuan_pc_tidak_ada)
        pc_server2 = Node("Apakah Anda ingin server Mid-Level?", yes_node=server2, no_node=pc_server3)
        pc_server1 = Node("Apakah Anda ingin server Entry-Level?", yes_node=server1, no_node=pc_server2)
        
        produktivitas3 = Node("Apakah untuk kebutuhan coding dan Android Studio?", yes_node=budget1, no_node=tujuan_pc_tidak_ada)
        produktivitas2 = Node("Apakah untuk kebutuhan editing?", yes_node=budget1, no_node=produktivitas3)
        produktivitas1 = Node("Apakah untuk kebutuhan Ms Family, video, dan streaming?", yes_node=budget1, no_node=produktivitas2)

        
        tujuan_pc4 = Node("Apakah anda merakit pc untuk server ?", yes_node=pc_server1, no_node=tujuan_pc_tidak_ada)
        tujuan_pc3 = Node("Apakah anda merakit pc untuk konten kreator ?", yes_node=pc_creator1, no_node=tujuan_pc4)
        tujuan_pc2 = Node("Apakah anda merakit pc untuk gaming ?", yes_node=gaming1, no_node=tujuan_pc3)
        tujuan_pc1 = Node("Apakah anda merakit pc untuk produktivitas ?", yes_node=produktivitas1, no_node=tujuan_pc2)
        
        return tujuan_pc1

    def inferensia(node):
        while node.question:  # Selama masih ada pertanyaan
            jawaban = input(node.question + " (yes/no): ").lower()
            if jawaban == "yes":
                node = node.yes_node
            elif jawaban == "no":
                node = node.no_node
            else:
                print("Saya tidak mengerti, coba ketik 'yes' atau 'no'.")
        print("\nRakit PC:\n", node.hasil)


# Main program
if __name__ == "__main__":
    decision_tree = Node.build_tree()
    Node.inferensia(decision_tree)