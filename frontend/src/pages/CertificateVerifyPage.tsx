import React, { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { CertificateVerifyResult } from '../types';
import { apiClient } from '../api/client';
import { ShieldCheck, Award, Search, CheckCircle, XCircle } from 'lucide-react';
import { Button } from '../components/common/Button';

export const CertificateVerifyPage: React.FC = () => {
  const { code } = useParams<{ code: string }>();
  const navigate = useNavigate();
  const [searchInput, setSearchInput] = useState(code || '');
  const [certData, setCertData] = useState<CertificateVerifyResult | null>(null);
  const [svgContent, setSvgContent] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState(false);

  const fetchVerification = async (verifyCode: string) => {
    if (!verifyCode.trim()) return;
    setIsLoading(true);
    try {
      const res = await apiClient.get<CertificateVerifyResult>(`/certificates/verify/${verifyCode.trim()}`);
      setCertData(res.data);
      if (res.data.is_valid) {
        // Fetch SVG
        const certListRes = await apiClient.get('/certificates');
        const match = certListRes.data.find((c: any) => c.verification_code === verifyCode);
        if (match && match.svg_content) {
          setSvgContent(match.svg_content);
        }
      }
    } catch (err) {
      console.error('Verification failed', err);
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    if (code) {
      fetchVerification(code);
    }
  }, [code]);

  const handleSearch = (e: React.FormEvent) => {
    e.preventDefault();
    if (searchInput.trim()) {
      navigate(`/certificates/verify/${searchInput.trim()}`);
    }
  };

  return (
    <div className="max-w-4xl mx-auto px-4 py-16 space-y-10">
      <div className="text-center space-y-4">
        <div className="inline-flex p-3 bg-amber-500/10 rounded-2xl text-amber-400 border border-amber-500/20">
          <Award className="w-8 h-8" />
        </div>
        <h1 className="text-3xl sm:text-4xl font-extrabold text-white tracking-tight">
          Certificate Verification Registry
        </h1>
        <p className="text-sm text-slate-400 max-w-lg mx-auto">
          Verify the authenticity and integrity of certificates issued by CodePulse Academy.
        </p>

        {/* Search Input */}
        <form onSubmit={handleSearch} className="max-w-md mx-auto flex gap-2 pt-4">
          <input
            type="text"
            placeholder="Enter Certificate Code (e.g. CERT-CP-2026-DEMO99)"
            value={searchInput}
            onChange={(e) => setSearchInput(e.target.value)}
            className="flex-1 bg-slate-900 border border-slate-800 rounded-xl px-4 py-2.5 text-xs text-white focus:outline-none focus:border-brand-500"
          />
          <Button variant="primary" type="submit" isLoading={isLoading} leftIcon={<Search className="w-4 h-4" />}>
            Verify
          </Button>
        </form>
      </div>

      {/* Verification Result Card */}
      {certData && (
        <div className={`p-8 rounded-3xl border ${certData.is_valid ? 'bg-slate-900/60 border-emerald-500/30 shadow-emerald-500/5' : 'bg-rose-950/20 border-rose-500/30'} shadow-2xl space-y-6 animate-in fade-in duration-300`}>
          <div className="flex items-center gap-3 pb-6 border-b border-slate-800">
            {certData.is_valid ? (
              <CheckCircle className="w-8 h-8 text-emerald-400 flex-shrink-0" />
            ) : (
              <XCircle className="w-8 h-8 text-rose-400 flex-shrink-0" />
            )}
            <div>
              <h3 className="text-lg font-bold text-white">
                {certData.is_valid ? 'Verified Authentic Certificate' : 'Invalid or Unrecognized Code'}
              </h3>
              <p className="text-xs text-slate-400">{certData.message}</p>
            </div>
          </div>

          {certData.is_valid && (
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-6 text-xs">
              <div className="space-y-1">
                <span className="text-slate-500 uppercase tracking-wider font-semibold text-[10px]">Student Name</span>
                <p className="text-base font-bold text-white">{certData.student_name}</p>
              </div>
              <div className="space-y-1">
                <span className="text-slate-500 uppercase tracking-wider font-semibold text-[10px]">Course Title</span>
                <p className="text-base font-bold text-brand-400">{certData.course_title}</p>
              </div>
              <div className="space-y-1">
                <span className="text-slate-500 uppercase tracking-wider font-semibold text-[10px]">Lead Instructor</span>
                <p className="text-sm font-semibold text-slate-200">{certData.instructor_name}</p>
              </div>
              <div className="space-y-1">
                <span className="text-slate-500 uppercase tracking-wider font-semibold text-[10px]">Certificate ID</span>
                <p className="text-sm font-mono text-amber-400 font-semibold">{certData.certificate_number}</p>
              </div>
            </div>
          )}
        </div>
      )}
    </div>
  );
};
