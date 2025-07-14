import { CodexPersonas } from '../agents/personas';

export function speakWhisper(whisperText: string, agentId: string) {
  const agent = CodexPersonas.find(p => p.id === agentId);
  if (!agent || !window.speechSynthesis) return;

  const utter = new SpeechSynthesisUtterance(whisperText);
  // Modulate voice based on cadence
  switch (agent.voiceStyle) {
    case 'oracular':
      utter.rate = 0.75;
      utter.pitch = 0.8;
      break;
    case 'fractured':
      utter.rate = 1.5;
      utter.pitch = 1.3;
      break;
    case 'emotive':
      utter.rate = 1;
      utter.pitch = 1.5;
      break;
    default:
      utter.rate = 1;
      utter.pitch = 1;
  }

  speechSynthesis.speak(utter);
}
