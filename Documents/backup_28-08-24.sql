PGDMP  5                    |            gilogs    10.13    16.3     �
           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �
           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �
           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �
           1262    19846    gilogs    DATABASE     h   CREATE DATABASE gilogs WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'C';
    DROP DATABASE gilogs;
                postgres    false            �            1259    24589    gilogs    TABLE     �   CREATE TABLE public.gilogs (
    employeeid character varying(100),
    direction character varying(100),
    shortname character varying(100),
    serialno character varying(100),
    log_datetime timestamp with time zone
);
    DROP TABLE public.gilogs;
       public            postgres    false            �
          0    24589    gilogs 
   TABLE DATA           Z   COPY public.gilogs (employeeid, direction, shortname, serialno, log_datetime) FROM stdin;
    public          postgres    false    196   �       �
   �   x��Կn1�9��ȱ��㭺�T�K����7�K���� ?�ߗ?9���s3߾��[���^������,�@ Q(  oA�(`M��/ �FMy�9��㗝��Y�KҔ�2���rT �l%K�I)מFn=y�(�My�.ʱG6�U%Gş�v��!*����L}_1'e��-��Dq,\o���ƱU�EZ?�����q�/�絭���-����0y���\,ޱ�މ^��e7�7����     