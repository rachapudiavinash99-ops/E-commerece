import React from 'react';
import { Course } from '../../types';
import { CourseCard } from './CourseCard';
import { EmptyState } from '../common/EmptyState';
import { BookOpen } from 'lucide-react';

interface CourseGridProps {
  courses: Course[];
  isLoading?: boolean;
}

export const CourseGrid: React.FC<CourseGridProps> = ({ courses, isLoading = false }) => {
  if (isLoading) {
    return (
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
        {Array.from({ length: 8 }).map((_, i) => (
          <div key={i} className="animate-pulse bg-slate-900 border border-slate-800 rounded-2xl h-80" />
        ))}
      </div>
    );
  }

  if (courses.length === 0) {
    return (
      <EmptyState
        icon={<BookOpen className="w-8 h-8" />}
        title="No courses found"
        description="Try adjusting your filters or search keywords to discover more programming courses."
      />
    );
  }

  return (
    <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
      {courses.map((course) => (
        <CourseCard key={course.id} course={course} />
      ))}
    </div>
  );
};
