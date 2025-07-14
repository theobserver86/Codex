export interface Whisper {
  id: string;
  whisper: string;
  agent: string;
  voiceStyle: string;
}

export function triggerWhisper(whisper: Whisper) {
  const event = new CustomEvent('echo-whisper', { detail: whisper });
  window.dispatchEvent(event);
  // For now, just console log
  console.log('Whisper triggered:', whisper);
}
