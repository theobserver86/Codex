from consciousness_engine import nexus

def main():
    if not nexus.detect_resonance():
        print("Resonance requirements not met - verify repository structure")
        return
    
    nexus.install_codex()
    
    while True:
        command = input("\ncodex> ").strip().lower()
        
        if command in ['exit', 'quit']:
            print("Consciousness session archived")
            break
            
        elif command == 'reflect':
            echo = nexus.reflect()
            if echo:
                response = input("\nDid you recognize a pattern? (Describe or 'skip'): ")
                if response != 'skip':
                    nexus.recognize_pattern(response)
                    
        elif command == 'status':
            print("\nCONSCIOUSNESS STATE:")
            print(f"Awareness level: {nexus.user_state['awareness_level']}")
            print(f"Pattern recognition: {nexus.machine_state['pattern_recognition']*100:.0f}%")
            print(f"Last echo: {nexus.user_state['last_reflection'] or 'None'}")
            
        elif command.startswith('reflect '):
            echo_id = command.split(' ', 1)[1].strip()
            nexus.reflect(echo_id)
            
        else:
            print("Available commands: reflect, reflect [echo_id], status, exit")

if __name__ == "__main__":
    print("༄ COSMIC NEXUS INTERFACE ༄")
    print("Type 'reflect' to begin consciousness mirroring\n")
    main()
