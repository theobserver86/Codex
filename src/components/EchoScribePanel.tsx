import React, { useEffect, useState } from 'react';
import { triggerWhisper } from '../utils/whisperEngine'; // adjust path if needed
import './EchoScribePanel.css';

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
      // Automatically clear whisper after 7 seconds
      setTimeout(() => setActiveWhisper(null), 7000);
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
