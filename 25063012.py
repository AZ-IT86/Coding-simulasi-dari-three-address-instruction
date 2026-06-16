import re
import math

class ThreeAddressInstruction:
    """Simulasi Three Address Instruction (3-address)"""
    def __init__(self):
        self.instructions = []
        self.temp_counter = 0
        
    def generate_temp(self):
        """Generate temporary variable name"""
        self.temp_counter += 1
        return f"T{self.temp_counter}"
    
    def add_instruction(self, op, dest, src1, src2=None):
        """Tambahkan instruksi 3-address"""
        if src2:
            instr = f"{dest} = {src1} {op} {src2}"
        else:
            instr = f"{dest} = {op} {src1}"
        self.instructions.append(instr)
        return instr
    
    def execute(self, variables):
        """Eksekusi instruksi 3-address"""
        memory = variables.copy()
        
        print("\n=== THREE ADDRESS INSTRUCTION ===")
        print("Format: dest = src1 op src2")
        print("-" * 50)
        
        for instr in self.instructions:
            print(f"Execute: {instr}")
            
            # Parse instruksi
            if ' = ' in instr:
                parts = instr.split(' = ')
                dest = parts[0]
                expr = parts[1]
                
                # Evaluasi ekspresi
                if ' + ' in expr:
                    src1, src2 = expr.split(' + ')
                    src1_val = float(memory.get(src1.strip(), src1.strip()))
                    src2_val = float(memory.get(src2.strip(), src2.strip()))
                    result = src1_val + src2_val
                elif ' - ' in expr:
                    src1, src2 = expr.split(' - ')
                    src1_val = float(memory.get(src1.strip(), src1.strip()))
                    src2_val = float(memory.get(src2.strip(), src2.strip()))
                    result = src1_val - src2_val
                elif ' * ' in expr:
                    src1, src2 = expr.split(' * ')
                    src1_val = float(memory.get(src1.strip(), src1.strip()))
                    src2_val = float(memory.get(src2.strip(), src2.strip()))
                    result = src1_val * src2_val
                elif ' / ' in expr:
                    src1, src2 = expr.split(' / ')
                    src1_val = float(memory.get(src1.strip(), src1.strip()))
                    src2_val = float(memory.get(src2.strip(), src2.strip()))
                    if src2_val != 0:
                        result = src1_val / src2_val
                    else:
                        print("  Error: Division by zero!")
                        result = 0
                else:
                    # Assign langsung
                    result = float(memory.get(expr.strip(), expr.strip()))
                
                memory[dest] = result
                print(f"  Result: {dest} = {result}")
        
        return memory


class TwoAddressInstruction:
    """Simulasi Two Address Instruction (2-address)"""
    def __init__(self):
        self.instructions = []
        
    def add_instruction(self, op, dest, src):
        """Tambahkan instruksi 2-address"""
        instr = f"{dest} = {dest} {op} {src}"
        self.instructions.append(instr)
        return instr
    
    def execute(self, variables):
        """Eksekusi instruksi 2-address"""
        memory = variables.copy()
        
        print("\n=== TWO ADDRESS INSTRUCTION ===")
        print("Format: dest = dest op src")
        print("-" * 50)
        
        for instr in self.instructions:
            print(f"Execute: {instr}")
            
            # Parse instruksi: dest = dest op src
            parts = instr.split(' = ')
            dest = parts[0].strip()
            expr = parts[1].strip()
            
            # Parse: dest op src
            if ' + ' in expr:
                var, src = expr.split(' + ')
                src_val = float(memory.get(src.strip(), src.strip()))
                dest_val = float(memory.get(dest, 0))
                result = dest_val + src_val
            elif ' - ' in expr:
                var, src = expr.split(' - ')
                src_val = float(memory.get(src.strip(), src.strip()))
                dest_val = float(memory.get(dest, 0))
                result = dest_val - src_val
            elif ' * ' in expr:
                var, src = expr.split(' * ')
                src_val = float(memory.get(src.strip(), src.strip()))
                dest_val = float(memory.get(dest, 0))
                result = dest_val * src_val
            elif ' / ' in expr:
                var, src = expr.split(' / ')
                src_val = float(memory.get(src.strip(), src.strip()))
                dest_val = float(memory.get(dest, 0))
                if src_val != 0:
                    result = dest_val / src_val
                else:
                    print("  Error: Division by zero!")
                    result = 0
            else:
                result = float(memory.get(expr.strip(), expr.strip()))
            
            memory[dest] = result
            print(f"  Result: {dest} = {result}")
        
        return memory


class OneAddressInstruction:
    """Simulasi One Address Instruction (1-address) dengan accumulator"""
    def __init__(self):
        self.instructions = []
        self.accumulator = 0
        
    def add_instruction(self, op, operand=None):
        """Tambahkan instruksi 1-address"""
        if operand is not None:
            instr = f"{op} {operand}"
        else:
            instr = f"{op}"
        self.instructions.append(instr)
        return instr
    
    def execute(self, variables):
        """Eksekusi instruksi 1-address"""
        memory = variables.copy()
        acc = 0
        
        print("\n=== ONE ADDRESS INSTRUCTION ===")
        print("Format: LOAD X, ADD X, SUB X, MUL X, DIV X, STORE X")
        print("-" * 50)
        
        for instr in self.instructions:
            print(f"Execute: {instr}")
            
            parts = instr.split()
            op = parts[0]
            
            if op == "LOAD":
                operand = parts[1]
                acc = float(memory.get(operand, operand))
                print(f"  ACC = {acc}")
                
            elif op == "ADD":
                operand = parts[1]
                val = float(memory.get(operand, operand))
                old_acc = acc
                acc += val
                print(f"  ACC = {old_acc} + {val} = {acc}")
                
            elif op == "SUB":
                operand = parts[1]
                val = float(memory.get(operand, operand))
                old_acc = acc
                acc -= val
                print(f"  ACC = {old_acc} - {val} = {acc}")
                
            elif op == "MUL":
                operand = parts[1]
                val = float(memory.get(operand, operand))
                old_acc = acc
                acc *= val
                print(f"  ACC = {old_acc} * {val} = {acc}")
                
            elif op == "DIV":
                operand = parts[1]
                val = float(memory.get(operand, operand))
                old_acc = acc
                if val != 0:
                    acc /= val
                    print(f"  ACC = {old_acc} / {val} = {acc}")
                else:
                    print("  Error: Division by zero!")
                    
            elif op == "STORE":
                operand = parts[1]
                memory[operand] = acc
                print(f"  {operand} = {acc}")
                
            elif op == "STOP":
                print("  Program stopped")
                break
        
        self.accumulator = acc
        return memory


def validate_expression(expression):
    """Validasi ekspresi matematika"""
    # Hapus spasi untuk validasi
    expr = expression.replace(" ", "")
    
    # Cek apakah ekspresi kosong
    if not expr:
        return False, "Ekspresi tidak boleh kosong!"
    
    # Cek karakter yang diizinkan (hanya huruf, angka, operator, kurung, dan titik)
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+-*/(). ')
    for char in expression:
        if char not in allowed_chars:
            return False, f"Karakter '{char}' tidak diizinkan! Hanya huruf, angka, operator (+,-,*,/), dan kurung yang diperbolehkan."
    
    # Cek jumlah kurung
    if expression.count('(') != expression.count(')'):
        return False, "Jumlah kurung buka dan tutup tidak sama!"
    
    # Cek operator berurutan
    if re.search(r'[\+\-\*\/]{2,}', expr):
        return False, "Terdapat operator yang berurutan!"
    
    # Cek operator di awal (kecuali tanda negatif)
    if expr and expr[0] in '*/':
        return False, "Ekspresi tidak boleh dimulai dengan operator '*' atau '/'!"
    
    # Cek operator di akhir
    if expr and expr[-1] in '+-*/':
        return False, "Ekspresi tidak boleh diakhiri dengan operator!"
    
    # Cek validitas variabel (hanya huruf atau huruf dengan angka)
    tokens = re.findall(r'[A-Za-z]+[A-Za-z0-9]*', expr)
    for token in tokens:
        if not token.isalpha() and not token[0].isalpha():
            return False, f"Nama variabel '{token}' tidak valid! Variabel harus dimulai dengan huruf."
    
    return True, "Ekspresi valid"


def validate_variables(var_input):
    """Validasi input variabel"""
    variables = {}
    
    # Jika input kosong
    if not var_input.strip():
        return False, "Nilai variabel tidak boleh kosong!", variables
    
    # Split berdasarkan koma
    parts = [p.strip() for p in var_input.split(',') if p.strip()]
    
    if not parts:
        return False, "Format nilai variabel tidak valid!", variables
    
    for item in parts:
        # Cek apakah ada '='
        if '=' not in item:
            return False, f"Format '{item}' tidak valid! Gunakan format: Nama=Value", variables
        
        # Split berdasarkan '='
        name_value = item.split('=')
        if len(name_value) != 2:
            return False, f"Format '{item}' tidak valid! Gunakan format: Nama=Value", variables
        
        name = name_value[0].strip()
        value_str = name_value[1].strip()
        
        # Validasi nama variabel
        if not name or not name[0].isalpha():
            return False, f"Nama variabel '{name}' tidak valid! Harus dimulai dengan huruf.", variables
        
        # Validasi nilai (harus angka)
        try:
            value = float(value_str)
        except ValueError:
            return False, f"Nilai '{value_str}' untuk variabel '{name}' bukan angka yang valid!", variables
        
        variables[name] = value
    
    return True, "Variabel valid", variables


def validate_target(target, variables):
    """Validasi target variabel"""
    if not target or not target.strip():
        return False, "Target variabel tidak boleh kosong!"
    
    target = target.strip()
    
    # Validasi nama target
    if not target[0].isalpha():
        return False, f"Target '{target}' tidak valid! Harus dimulai dengan huruf."
    
    # Cek apakah target sudah ada di variabel
    if target in variables:
        return True, f"Target '{target}' valid (akan menimpa nilai yang ada)"
    else:
        return True, f"Target '{target}' valid (variabel baru akan dibuat)"
    
    return True, "Target valid"


def get_valid_input(prompt, validation_func, error_msg="Input tidak valid!", *args):
    """Fungsi umum untuk mendapatkan input yang valid"""
    max_attempts = 3
    attempts = 0
    
    while attempts < max_attempts:
        user_input = input(prompt).strip()
        
        if validation_func == validate_expression:
            is_valid, message = validate_expression(user_input)
        elif validation_func == validate_variables:
            is_valid, message, _ = validate_variables(user_input)
        elif validation_func == validate_target:
            is_valid, message = validate_target(user_input, args[0] if args else {})
        else:
            is_valid, message = validation_func(user_input)
        
        if is_valid:
            return user_input
        else:
            attempts += 1
            print(f"❌ {message}")
            if attempts < max_attempts:
                print(f"  Silakan coba lagi ({attempts}/{max_attempts})")
    
    print(f"\n❌ Terlalu banyak percobaan! Program akan keluar.")
    exit(1)


def generate_three_address_for_expression(expression, target, variables):
    """Generate three address code untuk ekspresi sederhana"""
    three = ThreeAddressInstruction()
    
    # Hapus spasi
    expr = expression.replace(" ", "")
    
    # Untuk kasus (A+B)*C
    if '(' in expr and ')' in expr:
        # Ekstrak bagian dalam kurung
        start = expr.index('(')
        end = expr.index(')')
        inner = expr[start+1:end]
        outer = expr[end+1:]
        
        # Cari operator di inner
        if '+' in inner:
            vars_inner = inner.split('+')
            if len(vars_inner) == 2:
                # T1 = A + B
                temp1 = three.generate_temp()
                three.add_instruction('+', temp1, vars_inner[0].strip(), vars_inner[1].strip())
                
                # Proses outer
                if '*' in outer:
                    outer_vars = outer.split('*')
                    if len(outer_vars) == 1:
                        three.add_instruction('*', target, temp1, outer_vars[0].strip())
                elif '/' in outer:
                    outer_vars = outer.split('/')
                    if len(outer_vars) == 1:
                        three.add_instruction('/', target, temp1, outer_vars[0].strip())
                elif '+' in outer:
                    outer_vars = outer.split('+')
                    if len(outer_vars) == 1:
                        three.add_instruction('+', target, temp1, outer_vars[0].strip())
                elif '-' in outer:
                    outer_vars = outer.split('-')
                    if len(outer_vars) == 1:
                        three.add_instruction('-', target, temp1, outer_vars[0].strip())
    
    # Untuk kasus sederhana tanpa kurung: A+B*C
    else:
        # Cari operator
        operators = []
        for char in expr:
            if char in '+-*/':
                operators.append(char)
        
        # Untuk kasus A+B*C (prioritas perkalian)
        if '*' in expr and '+' in expr:
            # Parse: A + B * C
            parts = expr.split('+')
            if len(parts) == 2:
                left = parts[0]
                right = parts[1]
                if '*' in right:
                    sub_parts = right.split('*')
                    if len(sub_parts) == 2:
                        # T1 = B * C
                        temp1 = three.generate_temp()
                        three.add_instruction('*', temp1, sub_parts[0].strip(), sub_parts[1].strip())
                        # Y = A + T1
                        three.add_instruction('+', target, left.strip(), temp1)
    
    return three


def generate_two_address_for_expression(expression, target, variables):
    """Generate two address code untuk ekspresi sederhana"""
    two = TwoAddressInstruction()
    
    # Untuk kasus (A+B)*C
    if '(' in expression and ')' in expression:
        # Ekstrak bagian dalam kurung
        start = expression.index('(')
        end = expression.index(')')
        inner = expression[start+1:end]
        outer = expression[end+1:]
        
        # Cari variabel di inner
        if '+' in inner:
            vars_inner = inner.split('+')
            if len(vars_inner) == 2:
                # Inisialisasi target dengan 0
                # Y = Y + A
                two.add_instruction('+', target, vars_inner[0].strip())
                # Y = Y + B
                two.add_instruction('+', target, vars_inner[1].strip())
                
                # Proses outer
                if '*' in outer:
                    outer_vars = outer.split('*')
                    if len(outer_vars) == 1:
                        two.add_instruction('*', target, outer_vars[0].strip())
                elif '/' in outer:
                    outer_vars = outer.split('/')
                    if len(outer_vars) == 1:
                        two.add_instruction('/', target, outer_vars[0].strip())
    
    return two


def generate_one_address_for_expression(expression, target, variables):
    """Generate one address code untuk ekspresi sederhana"""
    one = OneAddressInstruction()
    
    # Untuk kasus (A+B)*C
    if '(' in expression and ')' in expression:
        # Ekstrak bagian dalam kurung
        start = expression.index('(')
        end = expression.index(')')
        inner = expression[start+1:end]
        outer = expression[end+1:]
        
        if '+' in inner:
            vars_inner = inner.split('+')
            if len(vars_inner) == 2:
                # LOAD A
                one.add_instruction('LOAD', vars_inner[0].strip())
                # ADD B
                one.add_instruction('ADD', vars_inner[1].strip())
                
                # Proses outer
                if '*' in outer:
                    outer_vars = outer.split('*')
                    if len(outer_vars) == 1:
                        one.add_instruction('MUL', outer_vars[0].strip())
                elif '/' in outer:
                    outer_vars = outer.split('/')
                    if len(outer_vars) == 1:
                        one.add_instruction('DIV', outer_vars[0].strip())
                
                # STORE Y
                one.add_instruction('STORE', target)
    
    return one


def main():
    """Main program dengan input interaktif dan validasi"""
    
    print("=" * 70)
    print("SIMULASI THREE, TWO, DAN ONE ADDRESS INSTRUCTION")
    print("=" * 70)
    
    # Input ekspresi dengan validasi
    print("\n📝 Masukkan ekspresi matematika")
    print("Contoh: (A+B)*C atau A+B*C atau (X-Y)/Z")
    print("Catatan: Hanya huruf, angka, operator (+,-,*,/), dan kurung yang diizinkan")
    
    expression = get_valid_input("Ekspresi: ", validate_expression)
    
    # Input variabel dengan validasi
    print("\n📊 Masukkan nilai variabel (pisahkan dengan koma)")
    print("Contoh: A=5,B=3,C=4")
    print("Catatan: Nilai harus berupa angka (integer atau desimal)")
    
    var_input = get_valid_input("Nilai variabel: ", validate_variables)
    _, _, variables = validate_variables(var_input)
    
    # Tampilkan variabel yang diterima
    print("\n✅ Variabel yang diterima:")
    for name, value in variables.items():
        print(f"  {name} = {value}")
    
    # Input target variabel dengan validasi
    print("\n🎯 Masukkan variabel tujuan")
    print("Contoh: Y")
    print("Catatan: Nama variabel harus dimulai dengan huruf")
    
    target = get_valid_input("Target: ", validate_target, variables)
    
    # Tampilkan input
    print("\n" + "=" * 70)
    print("📋 INPUT YANG DITERIMA:")
    print(f"  Ekspresi: {expression}")
    print(f"  Variabel: {variables}")
    print(f"  Target: {target}")
    print("=" * 70)
    
    # Hitung nilai sebenarnya dengan aman
    try:
        # Buat environment yang aman untuk eval
        safe_dict = {k: v for k, v in variables.items()}
        safe_dict.update({'math': math, '__builtins__': {}})
        actual_result = eval(expression, {"__builtins__": {}}, safe_dict)
        print(f"\n✅ Hasil sebenarnya: {target} = {actual_result}")
    except ZeroDivisionError:
        print(f"\n⚠️  Ekspresi mengandung pembagian dengan nol!")
        actual_result = None
    except Exception as e:
        print(f"\n⚠️  Tidak dapat mengevaluasi ekspresi: {e}")
        actual_result = None
    
    # Inisialisasi variables untuk setiap metode
    three_vars = variables.copy()
    two_vars = {target: 0, **variables}
    one_vars = variables.copy()
    
    # Dictionary untuk menyimpan hasil
    results = {}
    
    # ============ THREE ADDRESS ============
    print("\n" + "=" * 70)
    try:
        three = generate_three_address_for_expression(expression, target, variables)
        result_three = three.execute(three_vars)
        if target in result_three:
            results['Three Address'] = result_three[target]
            print(f"\n✅ Hasil (3-address): {target} = {result_three[target]}")
    except Exception as e:
        print(f"\n❌ Error pada Three Address: {e}")
        result_three = {}
    
    # ============ TWO ADDRESS ============
    print("\n" + "=" * 70)
    try:
        two = generate_two_address_for_expression(expression, target, variables)
        result_two = two.execute(two_vars)
        if target in result_two:
            results['Two Address'] = result_two[target]
            print(f"\n✅ Hasil (2-address): {target} = {result_two[target]}")
    except Exception as e:
        print(f"\n❌ Error pada Two Address: {e}")
        result_two = {}
    
    # ============ ONE ADDRESS ============
    print("\n" + "=" * 70)
    try:
        one = generate_one_address_for_expression(expression, target, variables)
        result_one = one.execute(one_vars)
        if target in result_one:
            results['One Address'] = result_one[target]
            print(f"\n✅ Hasil (1-address): {target} = {result_one[target]}")
    except Exception as e:
        print(f"\n❌ Error pada One Address: {e}")
        result_one = {}
    
    # ============ RINGKASAN HASIL AKHIR ============
    print("\n" + "=" * 70)
    print("📊 RINGKASAN HASIL AKHIR")
    print("=" * 70)
    
    if results:
        print(f"\nEkspresi: {expression}")
        print(f"Target: {target}")
        print("\nHasil dari setiap metode:")
        for method, value in results.items():
            print(f"  {method}: {target} = {value:.4f}")
        
        # Cek konsistensi hasil
        values = list(results.values())
        if len(values) > 1:
            all_same = all(abs(values[0] - v) < 0.0001 for v in values[1:])
            if all_same:
                print(f"\n✅ Semua metode menghasilkan hasil yang sama: {target} = {values[0]:.4f}")
                if actual_result is not None:
                    if abs(values[0] - actual_result) < 0.0001:
                        print(f"✅ Hasil sesuai dengan perhitungan sebenarnya")
                    else:
                        print(f"⚠️  Perbedaan dengan perhitungan sebenarnya!")
                        print(f"  Hasil program: {values[0]:.4f}")
                        print(f"  Hasil sebenarnya: {actual_result:.4f}")
            else:
                print("\n⚠️  Hasil berbeda-beda!")
        else:
            print(f"\nℹ️  Hanya satu metode yang berhasil menghasilkan hasil")
            if actual_result is not None:
                if abs(values[0] - actual_result) < 0.0001:
                    print(f"✅ Hasil sesuai dengan perhitungan sebenarnya")
                else:
                    print(f"⚠️  Perbedaan dengan perhitungan sebenarnya!")
    else:
        print("\n❌ Tidak ada metode yang berhasil menghasilkan hasil")
    
    print("\n" + "=" * 70)
    print("👋 Program selesai. Terima kasih!")


if __name__ == "__main__":
    main()