import React from 'react';
import { Star } from 'lucide-react';

interface RatingStarsProps {
  rating: number;
  maxStars?: number;
  size?: number;
  showScore?: boolean;
  reviewCount?: number;
  onRate?: (score: number) => void;
  interactive?: boolean;
}

export const RatingStars: React.FC<RatingStarsProps> = ({
  rating,
  maxStars = 5,
  size = 16,
  showScore = true,
  reviewCount,
  onRate,
  interactive = false
}) => {
  const stars = Array.from({ length: maxStars }, (_, i) => i + 1);

  return (
    <div className="flex items-center gap-1.5">
      <div className="flex items-center">
        {stars.map((star) => {
          const isFilled = star <= Math.round(rating);
          return (
            <Star
              key={star}
              size={size}
              className={`${
                isFilled ? 'text-amber-400 fill-amber-400' : 'text-slate-600'
              } ${interactive ? 'cursor-pointer hover:text-amber-300 hover:fill-amber-300 transition-colors' : ''}`}
              onClick={() => interactive && onRate && onRate(star)}
            />
          );
        })}
      </div>
      {showScore && (
        <span className="text-xs font-bold text-amber-400">
          {rating.toFixed(1)}
        </span>
      )}
      {reviewCount !== undefined && (
        <span className="text-xs text-slate-400">
          ({reviewCount.toLocaleString()})
        </span>
      )}
    </div>
  );
};
