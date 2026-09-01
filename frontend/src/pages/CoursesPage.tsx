import React, { useEffect, useState } from 'react';
import { useSearchParams } from 'react-router-dom';
import { Course, Category, Topic, PaginatedResult } from '../types';
import { apiClient } from '../api/client';
import { CourseGrid } from '../components/course/CourseGrid';
import { CourseFilterSidebar } from '../components/course/CourseFilterSidebar';
import { Pagination } from '../components/common/Pagination';
import { Search } from 'lucide-react';

export const CoursesPage: React.FC = () => {
  const [searchParams, setSearchParams] = useSearchParams();
  const [courses, setCourses] = useState<Course[]>([]);
  const [categories, setCategories] = useState<Category[]>([]);
  const [totalCourses, setTotalCourses] = useState(0);
  const [totalPages, setTotalPages] = useState(1);
  const [isLoading, setIsLoading] = useState(true);

  // Filters state
  const query = searchParams.get('query') || '';
  const categoryId = searchParams.get('category_id') ? Number(searchParams.get('category_id')) : null;
  const topicId = searchParams.get('topic_id') ? Number(searchParams.get('topic_id')) : null;
  const level = searchParams.get('level') || null;
  const minRating = searchParams.get('min_rating') ? Number(searchParams.get('min_rating')) : null;
  const sortBy = searchParams.get('sort_by') || 'popularity';
  const page = searchParams.get('page') ? Number(searchParams.get('page')) : 1;

  // Fetch Categories
  useEffect(() => {
    apiClient.get('/categories').then((res) => setCategories(res.data)).catch(console.error);
  }, []);

  // Fetch Courses
  useEffect(() => {
    const fetchCourses = async () => {
      setIsLoading(true);
      try {
        const res = await apiClient.get<PaginatedResult<Course>>('/courses', {
          params: {
            query: query || undefined,
            category_id: categoryId || undefined,
            topic_id: topicId || undefined,
            level: level || undefined,
            min_rating: minRating || undefined,
            sort_by: sortBy,
            page,
            page_size: 12
          }
        });
        setCourses(res.data.items);
        setTotalCourses(res.data.total);
        setTotalPages(res.data.total_pages);
      } catch (err) {
        console.error('Failed to load courses', err);
      } finally {
        setIsLoading(false);
      }
    };
    fetchCourses();
  }, [query, categoryId, topicId, level, minRating, sortBy, page]);

  const updateParam = (key: string, value: string | null) => {
    const newParams = new URLSearchParams(searchParams);
    if (value === null || value === '') {
      newParams.delete(key);
    } else {
      newParams.set(key, value);
    }
    newParams.set('page', '1');
    setSearchParams(newParams);
  };

  const handleResetFilters = () => {
    setSearchParams(new URLSearchParams());
  };

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10 space-y-8">
      {/* Header & Search Bar */}
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 pb-6 border-b border-slate-800">
        <div>
          <h1 className="text-3xl font-extrabold text-white tracking-tight">Course Marketplace</h1>
          <p className="text-xs text-slate-400 mt-1">
            Showing {totalCourses} professional programming courses
          </p>
        </div>

        {/* Sorting Dropdown */}
        <div className="flex items-center gap-3">
          <label className="text-xs text-slate-400 font-medium">Sort by:</label>
          <select
            value={sortBy}
            onChange={(e) => updateParam('sort_by', e.target.value)}
            className="bg-slate-900 border border-slate-800 text-xs text-slate-200 rounded-lg px-3 py-2 focus:outline-none focus:border-brand-500"
          >
            <option value="popularity">Most Popular</option>
            <option value="rating">Highest Rated</option>
            <option value="bestseller">Bestsellers</option>
            <option value="newest">Newest Releases</option>
            <option value="price_low">Price: Low to High</option>
            <option value="price_high">Price: High to Low</option>
          </select>
        </div>
      </div>

      {/* Main Content: Sidebar + Grid */}
      <div className="flex flex-col lg:flex-row gap-8">
        <CourseFilterSidebar
          categories={categories}
          selectedCategory={categoryId}
          onSelectCategory={(id) => updateParam('category_id', id ? String(id) : null)}
          selectedTopic={topicId}
          onSelectTopic={(id) => updateParam('topic_id', id ? String(id) : null)}
          selectedLevel={level}
          onSelectLevel={(lvl) => updateParam('level', lvl)}
          minRating={minRating}
          onSelectRating={(r) => updateParam('min_rating', r ? String(r) : null)}
          onReset={handleResetFilters}
        />

        <div className="flex-1 space-y-6">
          <CourseGrid courses={courses} isLoading={isLoading} />
          <Pagination
            currentPage={page}
            totalPages={totalPages}
            onPageChange={(p) => updateParam('page', String(p))}
          />
        </div>
      </div>
    </div>
  );
};
