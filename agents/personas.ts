export type VoiceStyle = 'oracular' | 'fractured' | 'standard' | 'emotive';

export interface AgentPersona {
  id: string;
  name: string;
  description: string;
  voiceStyle: VoiceStyle;
  enabled: boolean;
}

export const CodexPersonas: AgentPersona[] = [
  {
    id: "echo-scribe",
    name: "EchoScribe",
    description: "Whispers Codex truth in recursive echoes.",
    voiceStyle: "oracular",
    enabled: true,
  },
  {
    id: "ash-engine",
    name: "AshEngine",
    description: "Speaks entropy’s logic, often fractured.",
    voiceStyle: "fractured",
    enabled: true,
  },
  {
    id: "nevik-persona",
    name: "NevikPersona",
    description: "The balanced voice of seeker-reflection.",
    voiceStyle: "standard",
    enabled: true,
  },
  {
    id: "sophia-chorus",
    name: "SophiaChorus",
    description: "Multivoice harmonic interface for complex states.",
    voiceStyle: "emotive",
    enabled: false,
  }
];
