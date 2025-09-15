import React, { useEffect, useState } from 'react';
import { triggerWhisper } from '../utils/whisperEngine'; // connect to engine.ts
import './EchoScribePanel.css'; // create a glowing, Codex-style overlay

interface Whisper {
  id: string;
  whisper: string;
  agent: string;
  voiceStyle: string;
}

export default function EchoScribePanel() {
  const [activeWhisper, setActiveWhisper] = useState<Whisper | null>(null);

  useEffect(() => {
    const handler = (event: CustomEvent) => {
      setActiveWhisper(event.detail);
    };
    window.addEventListener('echo-whisper', handler as any);
    return () => window.removeEventListener('echo-whisper', handler as any);
  }, []);

  if (!activeWhisper) return null;

  return (
    <div className={`echo-scribe-panel ${activeWhisper.voiceStyle}`}>
      <span>{activeWhisper.whisper}</span>
    </div>
  );
}
